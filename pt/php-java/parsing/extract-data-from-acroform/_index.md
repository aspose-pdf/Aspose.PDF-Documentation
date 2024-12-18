---
title: Extrair dados de AcroForm 
linktitle: Extrair dados de AcroForm
type: docs
weight: 50
url: /pt/php-java/extract-data-from-acroform/
description: AcroForms existem em muitos documentos PDF. Este artigo tem como objetivo ajudá-lo a entender como extrair dados de AcroForms usando PHP e o Aspose.PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair campos de formulário de documento PDF

Aspose.PDF para PHP não só permite criar e preencher campos de formulário, mas também facilita a extração de dados de campos de formulário ou informações de campos de formulário de arquivos PDF.

Suponha que não conheçamos os nomes dos campos do formulário com antecedência. Então, devemos iterar sobre cada página no PDF para extrair informações sobre todos os AcroForms no PDF, bem como os valores dos campos do formulário. Para ter acesso ao formulário, precisamos usar o método [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```php

    // Criar uma nova instância da classe License e definir o arquivo de licença
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Definir o caminho para o diretório que contém o documento PDF
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // Definir o caminho para o arquivo PDF de entrada
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // Definir o cabeçalho da resposta para indicar que a resposta será no formato JSON
    header('Content-Type: application/json; charset=utf-8');

    // Inicializar a variável de dados da resposta
    $responseData = "";

    try {
        // Criar uma nova instância da classe Document e carregar o arquivo PDF de entrada
        $document = new Document($inputFile);

        // Obter os campos do formulário do documento e convertê-los para valores PHP
        $fields = java_values($document->getForm()->getFields());

        // Percorrer cada campo de formulário e extrair o nome e valor do campo
        foreach ($fields as $formField) {
            // Concatenar o nome e o valor do campo aos dados da resposta
            $responseData = $responseData . "(Nome do Campo: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Valor: " . $formField->getValue() . "),";
        }

        // Fechar o documento
        $document->close();
    }
```


Se você souber o nome dos campos do formulário dos quais deseja extrair valores, poderá usar o indexador na coleção Documents.Form para recuperar rapidamente esses dados.

## Extrair Dados para XML de um Arquivo PDF

A classe Form permite exportar dados para um arquivo XML a partir do arquivo PDF usando o método ExportXml. Para exportar dados para XML, você precisa criar um objeto da classe Form e, em seguida, chamar o método ExportXml usando o objeto FileStream. Finalmente, você pode fechar o objeto FileStream e descartar o objeto Form. O snippet de código a seguir mostra como exportar dados para um arquivo XML.

```php

    // Abrir documento
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Criar um objeto FileOutputStream para escrever o arquivo de fonte.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // Exportar dados
    $form->exportXml($xmlOutputStream);

    // Fechar fluxo de arquivo
    $xmlOutputStream->close();

    // Fechar o documento
    $form->close();
```

## Exportar Dados para FDF de um Arquivo PDF

Para exportar dados de formulários PDF para um arquivo XFDF, podemos usar o método [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) na classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Por favor, note que é uma classe de `com.aspose.pdf.facades`. Apesar do nome semelhante, esta classe tem um propósito ligeiramente diferente.

Para exportar dados para FDF, você precisa criar um objeto da classe `Form` e então chamar o método `exportXfdf` usando o objeto `OutputStream`. O trecho de código a seguir mostra como exportar dados para um arquivo XFDF.

```php

    // Abrir documento
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Criar um objeto FileOutputStream para escrever o arquivo de fonte.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // Exportar dados
    $form->exportFdf($xmlOutputStream);

    // Fechar fluxo de arquivo
    $xmlOutputStream->close();

    // Fechar o documento
    $form->close();
```

## Exportar Dados para XFDF de um Arquivo PDF

Para exportar dados de formulários PDF para um arquivo XFDF, podemos usar o método [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) na classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Para exportar dados para XFDF, você precisa criar um objeto da classe `Form` e então chamar o método `exportXfdf` usando o objeto `OutputStream`. 
O trecho de código a seguir mostra como exportar dados para um arquivo XFDF.

```php

    // Abrir documento
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Criar um objeto FileOutputStream para escrever o arquivo de fonte.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // Exportar dados
    $form->exportXfdf($xmlOutputStream);

    // Fechar fluxo de arquivo
    $xmlOutputStream->close();

    // Fechar o documento
    $form->close();
```