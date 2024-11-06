---
title: Convert Text to PDF 
linktitle: Convert Text to PDF
type: docs
weight: 300
url: pt/androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF para Android via Java permite converter arquivo de texto simples para PDF ou converter arquivo de texto pré-formatado para PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF para Android via Java** fornece a capacidade de converter arquivos de texto para o formato PDF. Neste artigo, demonstramos como podemos converter de forma fácil e eficiente um arquivo de texto para PDF usando o Aspose.PDF.

Quando você precisa converter um arquivo de texto para PDF, inicialmente leia o arquivo de texto de origem em algum leitor.
 Utilizamos StringBuilder para ler o conteúdo do arquivo de texto. Instancie o objeto Document e adicione uma nova página na coleção Pages. Crie um novo objeto de TextFragment e passe o objeto StringBuilder para seu construtor. Adicione um novo parágrafo na coleção Paragraphs usando o objeto TextFragment e salve o arquivo PDF resultante usando o método Save da classe Document.

## Converter arquivo de texto simples para PDF

```java
public void convertTXTtoPDF_Simple () {
        // Inicializar objeto de documento

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // Instanciar um objeto Document chamando seu construtor vazio
        document=new Document();

        // Adicionar uma nova página na coleção Pages do Document
        Page page=document.getPages().add();

        String string;
        StringBuilder stringBuilder=new StringBuilder();
        InputStream is;
        try {
            is=new FileInputStream(txtDocumentFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));
        while (true) {
            try {
                if ((string=reader.readLine()) == null) break;
            } catch (IOException e) {
                resultMessage.setText(e.getMessage());
                return;
            }
            stringBuilder.append(string).append("\n");
        }
        try {
            is.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Criar uma instância de TextFragment e passar o texto do objeto reader para seu
        // construtor como argumento
        TextFragment text=new TextFragment(stringBuilder.toString());

        // Adicionar um novo parágrafo de texto na coleção de parágrafos e passar o objeto
        // TextFragment
        page.getParagraphs().add(text);

        // Salvar o arquivo PDF resultante
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Converter arquivo de texto pré-formatado para PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // Leia o arquivo de texto como array de string
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instancie um objeto Document chamando seu construtor vazio
        document=new Document();

        // Adicione uma nova página na coleção Pages do Document
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // Defina margens esquerda e direita para melhor apresentação
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // verifique se a linha contém o caractere "form feed"
            // veja https://pt.wikipedia.org/wiki/Quebra_de_p%C3%A1gina
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Crie uma instância de TextFragment e
                // passe a linha para seu
                // construtor como argumento
                TextFragment text=new TextFragment(line);

                // Adicione um novo parágrafo de texto na coleção de parágrafos e passe o objeto
                // TextFragment
                page.getParagraphs().add(text);
            }
        }
        // Salve o arquivo PDF resultante
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```