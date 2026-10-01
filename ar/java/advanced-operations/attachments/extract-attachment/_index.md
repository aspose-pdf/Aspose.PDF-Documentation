---
title: استخراج المرفقات من PDF
linktitle: استخراج المرفقات
type: docs
weight: 50
url: /ar/java/extract-attachment/
description: تعلم كيفية استخراج الملفات المضمّنة وتعليقات مرفقات الملفات من مستندات PDF باستخدام Java و Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج ملف واحد أو جميع الملفات المضمّنة من PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخراج المرفقات من مستندات PDF باستخدام Aspose.PDF for Java. وتغطي استخراج مرفق واحد مسمى، حفظ كل ملف مضمّن إلى مجلد الإخراج، قراءة بيانات تعريف الملف، وتصدير المحتوى من تعليقة FileAttachment على صفحة.
---
يدعم Aspose.PDF for Java عدة تدفقات استخراج اعتمادًا على طريقة تخزين المرفقات في المستند.

## استخراج مرفق واحد بالاسم

استخدم هذا المثال عندما تحتاج إلى حفظ ملف مضمّن محدد واحد من ملف PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تكرار عبر مجموعة الملفات المضمّنة حتى يتم العثور على اسم المرفق المطلوب.
1. انسخ تدفق المرفق إلى ملف الإخراج وتوقف بعد الاستخراج.

```java
public static void extractSingleAttachment(Path inputFile, String attachmentName, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Extracting attachment: " + attachmentName);

        boolean attachmentFound = false;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            if (attachmentName.equals(fileSpecification.getName())) {
                try (InputStream inputStream = fileSpecification.getContents();
                     OutputStream outputStream = Files.newOutputStream(outputFile)) {
                    inputStream.transferTo(outputStream);
                }
                System.out.println("Attachment extracted successfully");
                attachmentFound = true;
                break;
            }
        }

        if (!attachmentFound) {
            throw new IllegalArgumentException("Attachment '" + attachmentName + "' not found in PDF");
        }
    }
}
```

## طباعة معلمات الملف المضمن

تقوم هذه الطريقة المساعدة بطباعة البيانات التعريفية المخزنة في [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/) كائن.

1. تحقق مما إذا كان كائن معلمات الملف موجودًا.
1. اقرأ قيمة مجموع التحقق المتاح، تاريخ الإنشاء، تاريخ التعديل، وقيم الحجم.
1. اطبع القيم إلى وحدة التحكم.

```java
public static void printFileParams(FileParams params) {
    if (params != null) {
        try {
            System.out.println("CheckSum: " + params.getCheckSum());
        } catch (Exception ex) {
            System.out.println("CheckSum: null");
        }
        System.out.println("Creation Date: " + params.getCreationDate());
        System.out.println("Modification Date: " + params.getModDate());
        System.out.println("Size: " + params.getSize());
    }
}
```

## استخراج جميع المرفقات المدمجة

استخدم هذا المثال عندما يجب كتابة كل ملف مضمّن في PDF إلى دليل إخراج.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر مجموعة الملفات المضمّنة وحدد اسم ملف إخراج آمن لكل عنصر.
1. اطبع البيانات الوصفية، احفظ كل تدفق مرفق، واستمر حتى يتم تصدير جميع الملفات.

```java
public static void extractAttachments(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Total files: " + document.getEmbeddedFiles().size());

        int fileIndex = 1;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            String fileName = fileSpecification.getName();
            if (fileName == null || fileName.isBlank()) {
                fileName = fileSpecification.getUnicodeName();
            }
            if (fileName == null || fileName.isBlank()) {
                fileName = "attachment_" + fileIndex + ".bin";
            }

            System.out.println("Name: " + fileName);
            System.out.println("Description: " + fileSpecification.getDescription());
            System.out.println("Mime Type: " + fileSpecification.getMIMEType());
            printFileParams(fileSpecification.getParams());

            Path outputPath = outputDir.resolve(fileName);
            try (InputStream inputStream = fileSpecification.getContents();
                 OutputStream outputStream = Files.newOutputStream(outputPath)) {
                inputStream.transferTo(outputStream);
            }
            fileIndex++;
        }
    }
}
```

## استخراج ملاحظة مرفق ملف

استخدم هذا المثال عندما يتم إرفاق الملف عبر ملاحظة صفحة بدلاً من فقط عبر مجموعة الملفات المضمَّنة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد الأول [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) على الصفحة.
1. اقرأ مواصفات الملف الخاصة به، صدّر المحتويات، واطبع مسار الوجهة.

```java
public static void extractFileAttachmentAnnotation(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        FileAttachmentAnnotation fileAttachment = null;
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FileAttachment) {
                fileAttachment = (FileAttachmentAnnotation) annotation;
                break;
            }
        }

        if (fileAttachment == null) {
            System.out.println("File attachment annotation not found.");
            return;
        }

        FileSpecification fileSpecification = fileAttachment.getFile();
        System.out.println("File name: " + fileSpecification.getName());

        Path outputPath = outputDir.resolve("extracted-" + fileSpecification.getName());
        try (InputStream inputStream = fileSpecification.getContents();
             OutputStream outputStream = Files.newOutputStream(outputPath)) {
            inputStream.transferTo(outputStream);
        }

        System.out.println("Extracted to: " + outputPath);
    }
}
```
