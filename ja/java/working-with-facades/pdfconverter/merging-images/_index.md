---
title: 画像をマージする
type: docs
weight: 10
url: /ja/java/merge-images/
description: このセクションでは画像をマージする方法について説明し、Tiff形式で保存することが可能です。
lastmod: "2021-07-01"
draft: false
---

Aspose.PDF 21.4では、画像を結合することができます。[画像をマージする](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfconverter/methods/mergeimages)メソッドは、特定のフォルダーの内容を確認し、その中の指定されたタイプのファイルを扱います。画像をマージする際には、'inputImagesStreams'、画像フォーマット、およびファイルの画像マージモード（例：垂直）を指定します。そして、結果をFileOutputStreamに保存します。

次のコードスニペットに従ってタスクを解決してください：

## 画像をマージする

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


二番目の例は前の例と同じように動作しますが、結合された画像は水平に保存されます。

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

三番目の例では、画像を中央に配置して結合します。
 水平に2つ、垂直に2つ。

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

また、Aspose.PDF for Javaは、[MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-)を使用して画像を結合し、Tiff形式で保存する機会を提供します。
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

PDFページに1つの画像として結合された画像を保存するために、imageStreamに配置し、配置したい座標を指定するaddImageメソッドで結果をページに配置します。

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