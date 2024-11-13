function lerMais() {
    alert("Aqui você poderá ler mais sobre o tema. Essa funcionalidade pode ser expandida para abrir o artigo completo.");
  }
  
  function adicionarComentario() {
    const comentarioInput = document.getElementById("comentarioInput");
    const comentariosLista = document.getElementById("comentariosLista");
  
    if (comentarioInput.value.trim() !== "") {
      const novoComentario = document.createElement("p");
      novoComentario.textContent = comentarioInput.value;
      comentariosLista.appendChild(novoComentario);
      comentarioInput.value = ""; 
    } else {
      alert("Digite um comentário antes de enviar.");
    }
  }