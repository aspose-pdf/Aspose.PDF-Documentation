---
title: Campos de botão e imagens
linktitle: Campos de botão e imagens
type: docs
weight: 40
url: /pt/java/button-fields-and-images/
description: Saiba como adicionar uma aparência de imagem a um campo de botão em um formulário PDF usando a fachada Form no Aspose.PDF for Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Adicionar uma aparência de imagem a um campo de botão PDF em Java
Abstract: Este artigo mostra como usar a fachada Form no Aspose.PDF for Java para vincular um formulário PDF, carregar uma imagem como fluxo, preencher um campo de botão de imagem e salvar o documento atualizado.
---
O exemplo Java em `FormExamples.addImageAppearanceToButtonField(...)` mostra como atualizar a aparência de um campo de botão com um fluxo de imagem.

O fluxo de trabalho é simples:

- vincular o PDF de entrada com `form.bindPdf(...)`
- abrir o arquivo de imagem com `Files.newInputStream(...)`
- chamada `form.fillImageField(...)` para o campo de botão
- salve o PDF atualizado

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
