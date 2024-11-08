---
title: Объединение изображений
type: docs
weight: 10
url: /ru/java/merge-images/
description: Этот раздел объясняет, как объединять изображения, и как сохранить их в формате Tiff.
lastmod: "2021-07-01"
draft: false
---

Aspose.PDF 21.4 позволяет объединять изображения. Метод [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) проверяет содержимое конкретной папки и работает с указанным типом файлов в ней. При работе с объединением изображений мы указываем 'inputImagesStreams', формат изображения и режим объединения изображений (например, вертикальный) нашего файла. Затем мы сохраняем наш результат в FileOutputStream.

Следуйте следующему фрагменту кода, чтобы решить вашу задачу:

## Объединение изображений

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


The second example works the same as the previous one, but the merged images will be saved horizontally.

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

В третьем примере мы объединим изображения, центрируя их.
 Два по горизонтали, два по вертикали.

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

Также Aspose.PDF для Java предоставляет вам возможность комбинировать изображения и сохранять их в формате Tiff, используя [MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).
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

Чтобы сохранить объединенные изображения как одно изображение на странице PDF, мы помещаем их в imageStream, размещаем результат на странице с помощью метода addImage, где указываем координаты, где хотим их разместить.

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