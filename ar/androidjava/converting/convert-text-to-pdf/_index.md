---
title: تحويل النص إلى PDF
linktitle: تحويل النص إلى PDF
type: docs
weight: 300
url: /ar/androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: يتيح لك Aspose.PDF لنظام Android عبر Java تحويل ملف نصي عادي إلى PDF أو تحويل ملف نصي مهيأ مسبقًا إلى PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF ومشاهدة النتائج عبر الإنترنت في هذا الرابط [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

يوفر **Aspose.PDF لنظام Android عبر Java** القدرة على تحويل ملفات النص إلى تنسيق PDF. في هذه المقالة، نوضح كيف يمكننا بسهولة وكفاءة تحويل ملف نصي إلى PDF باستخدام Aspose.PDF.

عندما تحتاج إلى تحويل ملف نصي إلى PDF، قم في البداية بقراءة ملف النص المصدر في بعض القارئ.
 لقد استخدمنا StringBuilder لقراءة محتويات ملف النص. قم بإنشاء كائن Document وأضف صفحة جديدة في مجموعة الصفحات. أنشئ كائن جديد من TextFragment ومرر كائن StringBuilder إلى منشئه. أضف فقرة جديدة في مجموعة الفقرات باستخدام كائن TextFragment واحفظ ملف PDF الناتج باستخدام طريقة Save لفئة Document.

## تحويل ملف نصي عادي إلى PDF

```java
public void convertTXTtoPDF_Simple () {
        // تهيئة كائن المستند

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // إنشاء كائن Document عن طريق استدعاء منشئه الفارغ
        document=new Document();

        // إضافة صفحة جديدة في مجموعة الصفحات للمستند
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


        // إنشاء مثيل لـ TextFragment وتمرير النص من كائن القارئ إلى منشئه كحجة
        TextFragment text=new TextFragment(stringBuilder.toString());

        // إضافة فقرة نصية جديدة في مجموعة الفقرات وتمرير كائن TextFragment
        page.getParagraphs().add(text);

        // حفظ ملف PDF الناتج
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## تحويل ملف نصي منسق مسبقًا إلى PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // قراءة الملف النصي كمصفوفة من السلاسل
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // إنشاء كائن Document عن طريق استدعاء منشئه الفارغ
        document=new Document();

        // إضافة صفحة جديدة في مجموعة Pages من Document
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // تعيين هوامش اليسار واليمين لتحسين العرض
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // التحقق مما إذا كانت السطر يحتوي على حرف "استمارة تغذية"
            // انظر https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // إنشاء مثيل من TextFragment و
                // تمرير السطر إلى منشئه
                // كحجة
                TextFragment text=new TextFragment(line);

                // إضافة فقرة نصية جديدة في مجموعة الفقرات وتمرير كائن TextFragment
                // الكائن
                page.getParagraphs().add(text);
            }
        }
        // حفظ ملف PDF الناتج
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```