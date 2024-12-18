---
title: Convertir Texto a PDF
linktitle: Convertir Texto a PDF
type: docs
weight: 300
url: /es/androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF para Android a través de Java te permite convertir un archivo de texto plano a PDF o convertir un archivo de texto preformateado a PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF para Android a través de Java** proporciona la capacidad de convertir archivos de texto a formato PDF. En este artículo, demostramos cuán fácil y eficientemente podemos convertir un archivo de texto a PDF usando Aspose.PDF.

Cuando necesites convertir un archivo de texto a PDF, inicialmente lee el archivo de texto fuente en algún lector.
 Hemos utilizado StringBuilder para leer el contenido del archivo de texto. Instanciar el objeto Document y agregar una nueva página en la colección Pages. Crear un nuevo objeto de TextFragment y pasar el objeto StringBuilder a su constructor. Agregar un nuevo párrafo en la colección Paragraphs utilizando el objeto TextFragment y guardar el archivo PDF resultante utilizando el método Save de la clase Document.

## Convertir archivo de texto plano a PDF

```java
public void convertTXTtoPDF_Simple () {
        // Inicializar objeto documento

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // Instanciar un objeto Document llamando a su constructor vacío
        document=new Document();

        // Agregar una nueva página en la colección Pages del Document
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

        // Crear una instancia de TextFragment y pasar el texto del objeto reader a su
        // constructor como argumento
        TextFragment text=new TextFragment(stringBuilder.toString());

        // Agregar un nuevo párrafo de texto en la colección paragraphs y pasar el objeto
        // TextFragment
        page.getParagraphs().add(text);

        // Guardar archivo PDF resultante
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Convertir archivo de texto preformateado a PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // Leer el archivo de texto como un array de cadenas
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar un objeto Document llamando a su constructor vacío
        document=new Document();

        // Agregar una nueva página a la colección Pages del Document
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // Establecer márgenes izquierdo y derecho para una mejor presentación
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // verificar si la línea contiene el carácter "form feed"
            // ver https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Crear una instancia de TextFragment y
                // pasar la línea a su
                // constructor como argumento
                TextFragment text=new TextFragment(line);

                // Agregar un nuevo párrafo de texto a la colección de párrafos y pasar el objeto
                // TextFragment
                page.getParagraphs().add(text);
            }
        }
        // Guardar el archivo PDF resultante
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```