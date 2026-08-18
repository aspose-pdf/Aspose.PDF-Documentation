---
title: استخراج المرفقات من PDF
linktitle: استخراج المرفقات
type: docs
weight: 50
url: /java/extract-attachment/
description: تعرف على كيفية استخراج الملفات المضمنة والتعليقات التوضيحية لمرفقات الملفات من مستندات PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم باستخراج واحد أو كل الملفات المضمنة من ملف PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخراج المرفقات من مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي استخراج مرفق واحد مسمى، وحفظ كل ملف مضمن في مجلد الإخراج، وقراءة البيانات التعريفية للملف، وتصدير المحتوى من التعليق التوضيحي FileAttachment على الصفحة.
---
يدعم Aspose.PDF for Java العديد من تدفقات الاستخراج اعتمادًا على كيفية تخزين المرفقات في المستند.

## استخراج مرفق واحد بالاسم

استخدم هذا المثال عندما تحتاج إلى حفظ ملف مضمن محدد من ملف PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار خلال مجموعة الملفات المضمنة حتى يتم العثور على اسم المرفق المطلوب.
1. انسخ دفق المرفقات إلى ملف الإخراج وتوقف بعد الاستخراج.

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

## طباعة معلمات الملف المضمنة

يقوم هذا الأسلوب المساعد بطباعة البيانات التعريفية المخزنة في كائن [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/).

1. تحقق من وجود كائن معلمات الملف.
1. اقرأ المجموع الاختباري المتاح وتاريخ الإنشاء وتاريخ التعديل وقيم الحجم.
1. طباعة القيم إلى وحدة التحكم.

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

## استخراج كافة المرفقات المضمنة

استخدم هذا المثال عندما يجب كتابة كل ملف مضمن في ملف PDF إلى دليل الإخراج.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار من خلال مجموعة الملفات المضمنة وحدد اسم ملف الإخراج الآمن لكل عنصر.
1. قم بطباعة البيانات التعريفية، واحفظ كل تدفق مرفق، واستمر حتى يتم تصدير جميع الملفات.

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

## استخراج تعليق توضيحي لمرفق الملف

استخدم هذا المثال عندما يتم إرفاق الملف من خلال تعليق توضيحي للصفحة بدلاً من فقط من خلال مجموعة الملفات المضمنة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد موقع [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) الأول على الصفحة.
1. اقرأ مواصفات الملف الخاص به، وقم بتصدير المحتويات، وطباعة مسار الوجهة.

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
