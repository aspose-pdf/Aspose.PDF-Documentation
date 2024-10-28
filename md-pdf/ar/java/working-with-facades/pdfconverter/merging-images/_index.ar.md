---
title: دمج الصور
type: docs
weight: 10
url: /java/merge-images/
description: يشرح هذا القسم كيفية دمج الصور، ومن الممكن الحفظ بتنسيق Tiff.
lastmod: "2021-07-01"
draft: false
---

يسمح Aspose.PDF 21.4 بدمج الصور. يقوم [دمج الصور](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) بفحص محتويات مجلد معين ويعمل مع نوع الملفات المحدد فيه. عند العمل مع دمج الصور، نحدد 'inputImagesStreams' وتنسيق الصورة وطريقة دمج الصور (كمثال - عمودي) لملفنا. ثم نحفظ نتيجتنا في FileOutputStream.

اتبع الجزء التالي من الشيفرة لحل مهمتك:

## دمج الصور

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


المثال الثاني يعمل بنفس طريقة المثال السابق، ولكن سيتم حفظ الصور المدمجة أفقيًا.

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

في المثال الثالث، سنقوم بدمج الصور عن طريق توسيطها.
 اثنين أفقيًا، اثنين عموديًا.

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

أيضًا، توفر لك Aspose.PDF for Java الفرصة لدمج الصور وحفظها بتنسيق Tiff، باستخدام [طريقة MergeImagesAsTiff](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).
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

لحفظ الصور المدمجة كصورة واحدة على صفحة PDF، نضعها في تيار الصور، ونضع النتيجة على الصفحة باستخدام طريقة addImage، حيث نحدد الإحداثيات التي نريد وضعها فيها.

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