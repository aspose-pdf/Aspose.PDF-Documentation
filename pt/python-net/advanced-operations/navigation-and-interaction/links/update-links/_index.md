---
title: Atualizar Links em PDF usando Python
linktitle: Atualizar Links
type: docs
weight: 20
url: /pt/python-net/update-links/
description: Atualizar links em PDF programaticamente. Este guia trata de como atualizar links em PDF na linguagem Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como atualizar Links em PDF
Abstract: O guia Aspose.PDF para Python via .NET sobre atualização de links orienta os desenvolvedores no processo de modificar o comportamento de hyperlinks em documentos PDF usando Python. Ele explica como alterar destinos de links para apontar a páginas específicas, sites externos ou até mesmo outros arquivos PDF. A documentação também aborda como ajustar a aparência das anotações de links, incluindo a cor do texto, e fornece exemplos de código práticos para cada cenário. Seja corrigindo URLs desatualizadas ou aprimorando a navegação, este recurso oferece uma abordagem clara e eficiente para gerenciar links programaticamente.
---

## Atualizar Cor de Texto da LinkAnnotation

Este exemplo mostra como detectar todas as anotações de link na primeira página de um PDF usando Aspose.PDF para Python, e então destacar o texto próximo a cada link alterando sua cor de fonte para vermelho. Ele utiliza TextFragmentAbsorber com uma área ligeiramente expandida ao redor de cada retângulo de link para encontrar e modificar o texto próximo.

Isso pode ser usado para:

- Marcação visual de links em um documento
- Melhorar a acessibilidade ao enfatizar o conteúdo vinculado
- Pré-processamento de arquivos PDF antes da revisão ou exportação

Para cada uma dessas anotações de link, o script recupera seu contorno retangular e expande ligeiramente essa região para incluir o texto próximo, permitindo uma identificação visual mais ampla. Em seguida, aplica um TextFragmentAbsorber sobre essa área expandida para extrair quaisquer fragmentos de texto localizados dentro dela. Esses fragmentos capturados são modificados alterando sua cor de fonte para vermelho, marcando efetivamente o texto ao redor para ênfase e revisão. Após aplicar todas essas atualizações, o documento modificado é salvo no caminho de saída, preservando as anotações destacadas e seu texto associado.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## Atualizar Borda

O script concentra-se na primeira página do documento e filtra todas as anotações, selecionando apenas aquelas do tipo LINK — estas geralmente representam elementos interativos, como hyperlinks ou gatilhos de navegação. Para cada uma dessas anotações de link, o código as converte para o tipo LinkAnnotation e atualiza sua propriedade de cor para vermelho, destacando-as visualmente para se sobressaírem ao restante do conteúdo. Após todas as anotações de link serem modificadas, o documento atualizado é salvo no local de saída definido, preservando o novo estilo.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## Atualizar Destino Web

Uma vez que os caminhos estejam configurados, o documento original é carregado usando a biblioteca Aspose.PDF, tornando seu conteúdo acessível para modificação. O script então foca na primeira página do documento, filtrando todas as anotações e selecionando apenas aquelas do tipo link, que tipicamente representam áreas clicáveis ou hyperlinks. Para evitar erros de tipo e garantir um manuseio seguro, cada anotação é verificada com is_assignable e então convertida para o tipo LinkAnnotation apropriado. Se o link estiver associado a um GoToURIAction, ou seja, apontando para um endereço web, o script atualiza esse URI para redirecionar os usuários para "https://www.google.com". Finalmente, após todas as alterações desejadas serem aplicadas, o documento modificado é salvo no caminho de saída especificado.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
