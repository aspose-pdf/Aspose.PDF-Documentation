---
title: Fusionar imágenes 
type: docs
weight: 10
url: /es/java/merge-images/
description: Esta sección explica cómo fusionar Imágenes, y es posible guardar en el formato Tiff.
lastmod: "2021-07-01"
draft: false
---

Aspose.PDF 21.4 permite combinar Imágenes. El método [Merge Images](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) verifica el contenido de una carpeta específica y trabaja con el tipo especificado de archivos en ella. Al trabajar con la fusión de imágenes, especificamos 'inputImagesStreams', el Formato de Imagen y el Modo de Fusión de Imagen (por ejemplo - vertical) de nuestro archivo. Luego guardamos nuestro resultado en FileOutputStream.

Sigue el siguiente fragmento de código para resolver tu tarea:

## Fusionar Imágenes

```java
 public static void MergeImages01() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImages(inputImagesStreams, com.aspose.pdf.ImageFormat.Jpeg,
                ImageMergeMode.Vertical, 1, 1);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
```      


El segundo ejemplo funciona igual que el anterior, pero las imágenes fusionadas se guardarán horizontalmente.

```java
   public static void MergeImages02() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) ->  name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImages(
            inputImagesStreams, 
            com.aspose.pdf.ImageFormat.Jpeg,
            ImageMergeMode.Horizontal, 1, 1);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

```

En el tercer ejemplo, fusionaremos las imágenes centrando las mismas.
 Dos horizontalmente, dos verticalmente.

```java
 public static void MergeImages03() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImages(inputImagesStreams, com.aspose.pdf.ImageFormat.Jpeg,
                ImageMergeMode.Center, 2, 2);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

```

Además, Aspose.PDF para Java te presenta la oportunidad de combinar imágenes y guardarlas en el formato Tiff, usando el [Método MergeImagesAsTiff](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).
```java
   public static void MergeImages04() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

```

Para guardar las imágenes fusionadas como una sola imagen en la página PDF, las colocamos en el imageStream, colocamos el resultado en la página con el método addImage, donde especificamos las coordenadas donde queremos colocarlas.

```java
    public static void MergeImages05()
    {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {                
                e.printStackTrace();
            }
        }

        InputStream imageStream = PdfConverter.mergeImages(inputImagesStreams, com.aspose.pdf.ImageFormat.Jpeg,
                ImageMergeMode.Vertical, 1, 1);
        
        Document document = new Document();
        Page page=document.getPages().add();
        page.addImage(imageStream, new Rectangle(10,120,400,720));
    }

```