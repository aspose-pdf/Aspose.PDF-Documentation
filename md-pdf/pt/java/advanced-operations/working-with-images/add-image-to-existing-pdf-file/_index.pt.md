---
title: Adicionar Imagem ao Arquivo PDF Existente
linktitle: Adicionar Imagem
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: Esta seção descreve como adicionar imagem a um arquivo PDF existente usando a biblioteca Java.
lastmod: "2021-06-05"
---

Cada página de PDF contém propriedades de Recursos e Conteúdos. Os recursos podem ser imagens e formulários, por exemplo, enquanto o conteúdo é representado por um conjunto de operadores PDF. Cada operador tem seu nome e argumento. Este exemplo usa operadores para adicionar uma imagem a um arquivo PDF.

Para adicionar uma imagem a um arquivo PDF existente:

- Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e abra o documento PDF de entrada.
- Obtenha a página à qual você deseja adicionar uma imagem.
- Adicione a imagem à coleção [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) da página.
- Use operadores para posicionar a imagem na página:
- Use o operador GSave para salvar o estado gráfico atual.

- Use o operador [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) para especificar onde a imagem deve ser colocada.
- Use o operador [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) para desenhar a imagem na página.
- Finalmente, use o operador [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) para salvar o estado gráfico atualizado.
- Salve o arquivo.

O trecho de código a seguir mostra como adicionar a imagem em um documento PDF.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // Abra um documento
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // Defina coordenadas
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // Obtenha a página onde você quer adicionar a imagem
        Page page = pdfDocument1.getPages().get_Item(1);

        // Carregue a imagem no fluxo
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // Adicione uma imagem à coleção de Imagens dos recursos da página
        page.getResources().getImages().add(imageStream);

        // Usando o operador GSave: este operador salva o estado gráfico atual
        page.getContents().add(new GSave());

        // Crie objetos Rectangle e Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem deve
        // ser posicionada
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Usando o operador Do: este operador desenha a imagem
        page.getContents().add(new Do(ximage.getName()));

        // Usando o operador GRestore: este operador restaura o estado gráfico
        page.getContents().add(new GRestore());

        // Salve o novo PDF
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // Feche o fluxo de imagem
        imageStream.close();
    }
```


## Adicionando imagem de BufferedImage em PDF

A partir do lançamento do Aspose.PDF para Java 9.5.0, introduzimos o suporte para adicionar imagem a partir de uma instância BufferedImage ao documento PDF. Para atender a esse requisito, um método foi implementado: [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
Você pode usar qualquer InputStream e não apenas o objeto FileInputStream para adicionar imagem. Assim, ao usar o objeto java.io.ByteArrayInputStream, você não precisa armazenar nenhum arquivo no sistema:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## Adicionar Imagem em um Arquivo PDF Existente (Facades)

Há também uma maneira alternativa e mais fácil de adicionar uma imagem a um arquivo PDF. Você pode usar o método AddImage da classe [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend). O método AddImage requer a imagem a ser adicionada, o número da página na qual a imagem precisa ser adicionada e a informação de coordenadas. Depois disso, salve o arquivo PDF atualizado usando o método Close.

O seguinte trecho de código mostra como adicionar uma imagem em um arquivo PDF existente.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // Abrir documento
        PdfFileMend mender = new PdfFileMend();

        // Criar objeto PdfFileMend para adicionar texto
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // Adicionar imagem no arquivo PDF
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // Salvar alterações
        mender.save(_dataDir + "AddImage_out.pdf");

        // Fechar objeto PdfFileMend
        mender.close();
    }
```


## Adicionar Referência de uma Única Imagem Várias Vezes em um Documento PDF

Às vezes, temos a necessidade de usar a mesma imagem várias vezes em um documento PDF. Adicionar uma nova instância aumenta o documento PDF resultante. Adicionamos um novo método XImageCollection.add(XImage) que suporta o objeto Ximage para adicionar na Coleção de Imagens. Este método permite adicionar referência ao mesmo objeto PDF como imagem original que otimiza o tamanho do Documento PDF.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## Identificar se a imagem dentro do PDF é Colorida ou Preto & Branco

Diferentes tipos de compressão podem ser aplicados sobre imagens para reduzir seu tamanho. O tipo de compressão aplicado sobre a imagem depende do ColorSpace da imagem de origem, ou seja, se a imagem for Colorida (RGB), então aplique compressão JPEG2000, e se for Preto & Branco, então a compressão JBIG2/JBIG2000 deve ser aplicada. Portanto, identificar cada tipo de imagem e usar um tipo apropriado de compressão criará um resultado melhor/otimizado.

Um arquivo PDF pode conter elementos como Texto, Imagem, Gráfico, Anexo, Anotação, etc., e se o arquivo PDF de origem contiver imagens, podemos determinar o espaço de cor da imagem e aplicar a compressão apropriada para a imagem para reduzir o tamanho do arquivo PDF. O trecho de código a seguir mostra as etapas para identificar se a imagem dentro do PDF é Colorida ou Preto & Branco.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // iterar por todas as páginas do arquivo PDF
            for (Page page : (Iterable<Page>) document.getPages()) {
                // criar instância de Image Placement Absorber
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* Tipo de Cor */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("Imagem em Tons de Cinza");
                        break;
                    case ColorType.Rgb:
                        System.out.println("Imagem Colorida");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("Erro ao ler o arquivo = " + document.getFileName());
        }
    }
}
```