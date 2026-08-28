document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector(".datalogo-navbar");
  const compactAt = 72;
  const expandAt = 18;

  const updateNavbarState = () => {
    if (!navbar) return;
    const isCompact = navbar.classList.contains("is-compact");

    if (!isCompact && window.scrollY > compactAt) {
      navbar.classList.add("is-compact");
      document.body.classList.add("nav-is-compact");
    }

    if (isCompact && window.scrollY < expandAt) {
      navbar.classList.remove("is-compact");
      document.body.classList.remove("nav-is-compact");
    }

    if (window.scrollY <= compactAt && window.scrollY >= expandAt) {
      document.body.classList.toggle("nav-is-compact", navbar.classList.contains("is-compact"));
    }
  };

  document.querySelectorAll("img.lazyload[data-src]").forEach((image) => {
    if (!image.getAttribute("src")) {
      image.setAttribute("src", image.dataset.src);
    }
  });

  const repository = document.querySelector("[data-ecosistema-repository]");
  if (repository) {
    // La ruta hacia la raiz del sitio la declara la propia pagina, porque las
    // paginas viven en html/ y los PDF cuelgan de la raiz.
    const base = repository.dataset.ecosistemaRepository || "";

    // Los datos llegan por <script> (data/ecosistema-documentos.js) para que el
    // repositorio tambien se vea al abrir el archivo desde una carpeta; el fetch
    // del .json queda como respaldo.
    const source = window.ECOSISTEMA_DOCUMENTOS
      ? Promise.resolve(window.ECOSISTEMA_DOCUMENTOS)
      : fetch(base + "data/ecosistema-documentos.json").then((response) => {
          if (!response.ok) {
            throw new Error("No se pudo cargar el repositorio.");
          }
          return response.json();
        });

    source
      .then((documents) => {
        // Los contadores del encabezado salen del propio repositorio, para que
        // no queden desactualizados cuando se agrega un documento nuevo.
        const total = document.querySelector("[data-ecosistema-total]");
        const diferencial = document.querySelector("[data-ecosistema-diferencial]");
        if (total) {
          total.textContent = documents.length;
        }
        if (diferencial) {
          diferencial.textContent = documents.filter(
            (item) => item.source === "Enfoque diferencial"
          ).length;
        }

        repository.innerHTML = "";
        documents.forEach((documentItem) => {
          const row = document.createElement("article");
          row.className = "knowledge-row";

          const thumb = document.createElement("a");
          thumb.className = "knowledge-thumb";
          thumb.href = base + encodeURI(documentItem.pdfPath);
          thumb.target = "_blank";
          thumb.rel = "noopener";

          const image = document.createElement("img");
          image.src = base + encodeURI(documentItem.thumbPath);
          image.alt = `Miniatura de ${documentItem.title}`;
          thumb.appendChild(image);

          const content = document.createElement("div");
          content.className = "knowledge-content";

          if (documentItem.category) {
            const tag = document.createElement("span");
            tag.className = "tag-differential";
            tag.textContent = documentItem.category;
            content.appendChild(tag);
          }

          const title = document.createElement("h3");
          const titleLink = document.createElement("a");
          titleLink.href = base + encodeURI(documentItem.pdfPath);
          titleLink.target = "_blank";
          titleLink.rel = "noopener";
          titleLink.textContent = documentItem.title;
          title.appendChild(titleLink);
          content.appendChild(title);

          const meta = document.createElement("div");
          meta.className = "knowledge-meta";
          const author = document.createElement("span");
          const authorLabel = document.createElement("strong");
          authorLabel.textContent = "Autor:";
          author.append(authorLabel, document.createTextNode("\u00a0"), documentItem.author || "No especificado");
          const year = document.createElement("span");
          const yearLabel = document.createElement("strong");
          yearLabel.textContent = "Año:";
          year.append(yearLabel, document.createTextNode("\u00a0"), documentItem.year);
          yearLabel.textContent = "A\u00f1o:";
          meta.append(author, year);
          content.appendChild(meta);

          const ideas = document.createElement("p");
          ideas.className = "knowledge-ideas";
          ideas.textContent = documentItem.ideas || "Información pendiente de incorporar.";
          content.appendChild(ideas);

          if (documentItem.sourceUrl) {
            const sourceLink = document.createElement("a");
            sourceLink.className = "knowledge-source";
            sourceLink.href = documentItem.sourceUrl;
            sourceLink.target = "_blank";
            sourceLink.rel = "noopener";
            sourceLink.textContent = "Consulta la publicación original";
            content.appendChild(sourceLink);
          }

          row.appendChild(thumb);
          row.appendChild(content);
          repository.appendChild(row);
        });
      })
      .catch(() => {
        repository.innerHTML = '<p class="repository-error">No fue posible cargar el repositorio de documentos.</p>';
      });
  }

  updateNavbarState();
  window.addEventListener("scroll", updateNavbarState, { passive: true });
});
