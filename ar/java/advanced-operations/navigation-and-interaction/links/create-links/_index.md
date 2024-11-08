---
title: إنشاء روابط في ملف PDF
linktitle: إنشاء روابط
type: docs
weight: 10
url: /ar/java/create-links/
description: يشرح هذا القسم كيفية إنشاء روابط في مستند PDF الخاص بك باستخدام Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إنشاء روابط

يسمح لك Aspose.PDF for Java بإضافة رابط إلى ملف PDF خارجي بحيث يمكنك ربط عدة مستندات معًا. من خلال إضافة رابط إلى تطبيق في مستند، من الممكن الربط بتطبيقات من مستند. هذا مفيد عندما تريد أن يقوم القراء بإجراء معين في نقطة معينة في البرنامج التعليمي، على سبيل المثال، أو لإنشاء مستند غني بالميزات. لإنشاء رابط لتطبيق:

1. [أنشئ مستندًا](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) كائن.
1. احصل على [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) التي تريد إضافة رابط إليها.

1. إنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) باستخدام كائنات [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) و[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. قم بتعيين خصائص الرابط باستخدام كائن [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. أيضًا، قم بتعيين إلى كائن [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) واستدعاء طريقة setAction(..).
1. عند إنشاء كائن [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction)، حدد التطبيق الذي تريد تشغيله.
1. أضف الرابط إلى مجموعة [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) الخاصة بكائن Page.
1. أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة Save الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

المقطع البرمجي التالي يوضح كيفية إنشاء رابط لتطبيق في ملف PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // افتح الوثيقة
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // إنشاء رابط
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // حفظ الوثيقة المحدثة
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### إنشاء رابط وثيقة PDF في ملف PDF

يتيح لك Aspose.PDF لـ Java إضافة رابط إلى ملف PDF خارجي بحيث يمكنك ربط عدة مستندات معًا.
 لإنشاء رابط لمستند PDF:

1. أولاً، قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. ثم، احصل على [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) المحددة التي تريد إضافة الرابط إليها.
1. قم بإنشاء كائن [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) باستخدام كائنات [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) و[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. قم بتعيين خصائص الرابط باستخدام كائن [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. قم باستدعاء طريقة setAction(..) ومرر كائن [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction).
1. أثناء إنشاء كائن [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction)، حدد ملف PDF الذي يجب تشغيله، وكذلك رقم الصفحة التي يجب فتحها.
1. أضف الرابط إلى مجموعة [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) الخاصة بكائن الصفحة.
2. وأخيرًا، احفظ ملف PDF المحدث باستخدام طريقة الحفظ الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يظهر مقتطف الشيفرة التالي كيفية إنشاء رابط مستند PDF في ملف PDF.

```java
    public static void CreatePDFDocumentLink() {

        // فتح المستند
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // إنشاء الرابط
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // حفظ المستند المحدث
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```