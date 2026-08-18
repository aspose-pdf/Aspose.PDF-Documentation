---
title: استخراج المحتوى الموسوم من ملفات PDF في Java
linktitle: استخراج المحتوى الموسوم
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: تعرف على كيفية فحص محتوى PDF ذي العلامات في Java باستخدام Aspose.PDF، بما في ذلك الوصول إلى المحتوى ذي العلامات، والوصول إلى البنية الجذرية، وعناصر البنية الفرعية.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
استخدم واجهات برمجة التطبيقات هذه عندما تحتاج إلى فحص شجرة البنية المنطقية لملف PDF ذي علامة تمييز وفحص أو تحديث البيانات التعريفية لعنصر البنية.

## احصل على البيانات الوصفية للمحتوى الموسوم

استخدم هذا المثال عندما تحتاج إلى الوصول إلى حاوية المحتوى ذات العلامات وتريد تحديد بيانات تعريف المستند الأساسية مثل العنوان واللغة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على الكائن [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) من المستند.
1. قم بتعيين بيانات تعريف المحتوى الموسومة واحفظ ملف الإخراج.

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## احصل على البنية الجذرية لملف PDF ذي علامة تمييز

يوضح هذا المثال كيفية فحص الكائنات الجذرية التي تمثل شجرة البنية لملف PDF ذو علامة تمييز.

1. قم بإنشاء ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) جديد واحصل على المحتوى المميز به.
1. قم بتعيين بيانات تعريف المستند المطلوبة.
1. قم بقراءة وطباعة جذر شجرة البنية وعنصر الجذر المنطقي، ثم احفظ الملف.

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## الوصول إلى عناصر البنية الفرعية وتحديثها

استخدم هذا المثال عندما تحتاج إلى تكرار العناصر الفرعية في شجرة البنية، وفحص خصائصها، وتحديث بيانات التعريف المحددة.

1. افتح المصدر الذي يحمل علامة PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ العناصر الفرعية من جذر شجرة الهيكل واطبع الخصائص المتاحة.
1. قم بالوصول إلى العناصر الفرعية للفرع الجذر الأول، وقم بتحديث بيانات التعريف الخاصة بها، واحفظ المستند.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```
