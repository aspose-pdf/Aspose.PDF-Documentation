---
title: Campos de botão e imagens
linktitle: Campos de botão e imagens
type: docs
weight: 40
url: /java/button-fields-and-images/
description: Aprenda como adicionar uma aparência de imagem a um campo de botão em um formulário PDF usando a fachada do formulário em Aspose.PDF para Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Adicione uma aparência de imagem a um campo de botão PDF em Java
Abstract: Este artigo mostra como usar a fachada do formulário no Aspose.PDF para Java para vincular um formulário PDF, carregar uma imagem como um fluxo, preencher um campo de botão de imagem e salvar o documento atualizado.
---
O exemplo Java em `FormExamples.addImageAppearanceToButtonField(...)` mostra como atualizar a aparência de um campo de botão com um fluxo de imagem.

O fluxo de trabalho é direto:

- vincule o PDF de entrada com `form.bindPdf(...)`
- abra o arquivo de imagem com `Files.newInputStream(...)`
- chame `form.fillImageField(...)` para o campo do botão
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
