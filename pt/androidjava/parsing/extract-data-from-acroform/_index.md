---
title:  Extrair dados do AcroForm
linktitle:  Extrair dados do AcroForm
type: docs
weight: 50
url: /pt/androidjava/extract-data-from-acroform/
description: AcroForms existem em muitos documentos PDF. Este artigo tem o objetivo de ajudá-lo a entender como extrair dados de AcroForms com o Aspose.PDF.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair campos de formulário do documento PDF

Aspose.PDF for Android via Java não só permite que você crie e preencha campos de formulário, mas também facilita a extração de dados de campos de formulário ou informações de campos de formulário de arquivos PDF.

Suponha que não conheçamos os nomes dos campos de formulário com antecedência. Então devemos iterar sobre cada página no PDF para extrair informações sobre todos os AcroForms no PDF, bem como os valores dos campos de formulário. Para ter acesso ao formulário, precisamos usar [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) método.

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

Se você souber o nome dos campos de formulário dos quais deseja extrair valores, então pode usar o indexador na coleção Documents.Form para recuperar esses dados rapidamente.

## Recuperar o valor do campo de formulário pelo título

A propriedade Value do campo de formulário permite obter o valor de um campo específico. Para obter o valor, obtenha o campo de formulário a partir do [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objeto's [coleção de campos de formulário](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). Este exemplo seleciona um [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) e recupera seu valor usando o [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) método.

```java

    public void extractFormDataByName () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```

## Extrair Dados para XML a partir de um Arquivo PDF

A classe Form permite que você exporte dados para um arquivo XML a partir do arquivo PDF usando o método ExportXml. Para exportar dados para XML, você precisa criar um objeto da classe Form e então chamar o método ExportXml usando o objeto FileStream. Finalmente, você pode fechar o objeto FileStream e descartar o objeto Form. O trecho de código a seguir mostra como exportar dados para um arquivo XML.

```java
public void extractFormFieldsToXML () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## Exportar Dados para FDF a partir de um Arquivo PDF

Para exportar os dados de formulários PDF para um arquivo XFDF, podemos usar o [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) método no [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) classe.

Observe que é uma classe de `com.aspose.pdf.facades`. Apesar do nome semelhante, esta classe tem um propósito ligeiramente diferente.

Para exportar dados para FDF, você precisa criar um objeto de `Form` classe e então chamar o `exportXfdf` método usando o `OutputStream` objeto. O trecho de código a seguir mostra como exportar dados para um arquivo XFDF.

```java
public void extractFormExportFDF () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Exportar Dados para XFDF de um Arquivo PDF

Para exportar os dados de formulários PDF para um arquivo XFDF, podemos usar o [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) método no [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) classe.

Para exportar dados para XFDF, você precisa criar um objeto de `Form` classe e então chamar o `exportXfdf` método usando o `OutputStream` objeto. 
O snippet de código a seguir mostra como exportar dados para um arquivo XFDF.

```java
    public void extractFormExportXFDF () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

