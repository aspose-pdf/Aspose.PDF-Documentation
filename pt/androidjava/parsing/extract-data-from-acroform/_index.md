---
title: Extrair dados de AcroForm
linktitle: Extrair dados de AcroForm
type: docs
weight: 50
url: /pt/androidjava/extract-data-from-acroform/
description: AcroForms existem em muitos documentos PDF. Este artigo visa ajudá-lo a entender como extrair dados de AcroForms com o Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair campos de formulário de documento PDF

Aspose.PDF para Android via Java não só permite que você crie e preencha campos de formulário, mas também facilita a extração de dados de campos de formulário ou informações de campos de formulário de arquivos PDF.

Suponha que não conheçamos os nomes dos campos de formulário com antecedência. Então devemos iterar sobre cada página no PDF para extrair informações sobre todos os AcroForms no PDF, bem como os valores dos campos de formulário. Para acessar o formulário, precisamos usar o método [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
 public void extractFormFields () {
        // Abrir documento
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obter valores de todos os campos
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Nome do Campo: ");
            sb.append(formField.getPartialName());
            sb.append(" Valor: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


Se você souber o nome dos campos de formulário dos quais deseja extrair valores, poderá usar o indexador na coleção Documents.Form para recuperar rapidamente esses dados.

## Recuperar valor do campo de formulário por título

A propriedade Value do campo de formulário permite que você obtenha o valor de um campo específico. Para obter o valor, obtenha o campo de formulário da [coleção de campos de formulário](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este exemplo seleciona um [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) e recupera seu valor usando o método [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java

    public void extractFormDataByName () {
        // Abrir documento
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


## Extrair Dados para XML de um Arquivo PDF

A classe Form permite exportar dados para um arquivo XML a partir do arquivo PDF usando o método ExportXml. Para exportar dados para XML, você precisa criar um objeto da classe Form e, em seguida, chamar o método ExportXml usando o objeto FileStream. Finalmente, você pode fechar o objeto FileStream e descartar o objeto Form. O trecho de código a seguir mostra como exportar dados para um arquivo XML.

```java
public void extractFormFieldsToXML () {
        // Abrir documento
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
            // Criar arquivo xml.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Exportar dados
            form.exportXml(xmlOutputStream);

            // Fechar fluxo de arquivo
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Fechar o documento
        form.dispose();
    }
```


## Exportar Dados para FDF de um Arquivo PDF

Para exportar dados de formulários PDF para um arquivo XFDF, podemos usar o método [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) na classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Por favor, note que é uma classe de `com.aspose.pdf.facades`. Apesar do nome semelhante, esta classe tem um propósito ligeiramente diferente.

Para exportar dados para FDF, você precisa criar um objeto da classe `Form` e então chamar o método `exportXfdf` usando o objeto `OutputStream`. O trecho de código a seguir mostra como exportar dados para um arquivo XFDF.

```java
public void extractFormExportFDF () {
        // Abrir documento
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

            // Exportar dados
            form.exportFdf(fdfOutputStream);

            // Fechar fluxo de arquivo
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Exportar Dados para XFDF de um Arquivo PDF

Para exportar dados de formulários PDF para um arquivo XFDF, podemos usar o método [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) na classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Para exportar dados para XFDF, você precisa criar um objeto da classe `Form` e então chamar o método `exportXfdf` usando o objeto `OutputStream`. O seguinte trecho de código mostra como exportar dados para um arquivo XFDF.

```java
    public void extractFormExportXFDF () {
        // Abrir documento
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

            // Exportar dados
            form.exportXfdf(fdfOutputStream);

            // Fechar fluxo do arquivo
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```