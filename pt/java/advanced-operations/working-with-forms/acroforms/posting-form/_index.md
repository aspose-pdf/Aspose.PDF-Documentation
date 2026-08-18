---
title: Publicação de formulários em PDF via Java
linktitle: Formulários de postagem
type: docs
weight: 75
url: /java/posting-form/
description: Adicione botões de envio e ações de envio ao PDF AcroForms usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione botões de envio e ações de postagem de formulário a arquivos PDF com Java
Abstract: Este artigo mostra como adicionar funcionalidade de envio a formulários PDF usando Aspose.PDF para Java. Ele cobre a criação de um botão de envio com FormEditor e a construção de um campo de botão personalizado que usa SubmitFormAction para obter mais controle sobre o URL e sinalizadores de envio.
---
Aspose.PDF para Java oferece suporte à criação de botões de envio baseados em fachada e em DOM.

## Adicione um botão de envio com FormEditor

1. Crie uma fachada [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) para o documento PDF de origem.
1. Adicione o objeto do botão de envio configurado por meio da fachada [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/).
1. Salve o documento PDF atualizado.

```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## Adicione uma ação de envio manualmente

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) e o URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. Crie o [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) na [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino e atribua a ação de envio.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```
