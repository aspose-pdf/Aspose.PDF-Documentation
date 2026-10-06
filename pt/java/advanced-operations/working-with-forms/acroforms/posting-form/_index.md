---
title: Publicando Formulários em PDF via Java
linktitle: Publicando Formulários
type: docs
weight: 75
url: /pt/java/posting-form/
description: Adicionar botões de envio e ações de submissão aos PDF AcroForms usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar botões de envio e ações de postagem de formulário a arquivos PDF com Java
Abstract: Este artigo mostra como adicionar funcionalidade de envio a formulários PDF usando Aspose.PDF for Java. Ele cobre a criação de um botão de envio com FormEditor e a construção de um campo de botão personalizado que utiliza SubmitFormAction para maior controle sobre a URL de submissão e as flags.
---
Aspose.PDF for Java suporta a criação de botões de envio baseados em facade e baseados em DOM.

## Adicionar um botão de envio com FormEditor

1. Criar um [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) fachada para o documento PDF de origem.
1. Adicionar o objeto do botão de envio configurado através da [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) fachada.
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

## Adicionar uma ação de envio manualmente

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) e URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. Crie o [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) no alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e atribua a ação de envio.
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
