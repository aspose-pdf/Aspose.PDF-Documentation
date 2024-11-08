---
title: ما الجديد
linktitle: ما الجديد
type: docs
weight: 10
url: /ar/java/whatsnew/
description: في هذه الصفحة يتم تقديم الميزات الجديدة الأكثر شهرة في Aspose.PDF لـ Java التي تم تقديمها في الإصدارات الأخيرة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## ما الجديد في Aspose.PDF 24.8

منذ الإصدار 24.8، دعم لصيغة PDF/A-4:

```java

    Document document = new Document(inputPdf);
    // يمكن فقط تحويل مستندات PDF-2.x إلى PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

أيضًا، من الممكن إضافة نص بديل لختم الصورة:

تمت إضافة خاصية AlternativeText إلى ImageStamp - إذا تم تعيين قيمة لها، فعند إضافة ImageStamp إلى مستند سيكون له نص بديل.

```java

    String p1_Alt1 = "*** الصفحة 1، نص بديل 1 ***",
                    p1_Alt2 = "*** الصفحة 1، نص بديل 2 ***",
                    p2_Alt1 = "--- الصفحة 1، نص بديل 1 ---",
                    p2_Alt2 = "--- الصفحة 1، نص بديل 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // إلى الصفحة 1
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // إلى الصفحة 2
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // حفظ المستند
    document.save(outFile);
```


أيضًا، يُظهر الكود التالي كيفية إضافة نص بديل في الصور الموجودة في عناصر الشكل.

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // تعيين نص بديل
            figureElement.setAlternativeText("Figure alternative text (technique 1)");
        }
    }

    // حفظ المستند
    document.save(outFile);
```


## ما الجديد في Aspose.PDF 24.7

منذ إصدار 24.7، كجزء من تحرير PDF الموسوم، تمت إضافة طرق على **Aspose.Pdf.LogicalStructure.Element**:

- Tag (إضافة وسوم إلى مشغلين محددين مثل الصور والنصوص والروابط)
- InsertChild
- RemoveChild
- ClearChilds

تتيح لك هذه الطرق تحرير وسوم ملفات PDF، على سبيل المثال:

```java

    Document document = new Document(dataDir + "test.pdf");

    // استرجاع الصفحة الأولى من المستند.
    Page page = document.getPages().get_Item(1);

    // تهيئة المتغيرات للاحتفاظ بعناصر BDC (سياق القاموس الابتدائي) لأغراض مختلفة.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // التجول عبر محتويات الصفحة.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // الحصول على المشغل الحالي من محتويات الصفحة.
        Operator op = page.getContents().get_Item(i);

        // التحقق مما إذا كان المشغل عبارة عن مثيل لـ BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // تحويل المشغل إلى نوع BDC.
        if (bdc != null)
        {
            // التحقق مما إذا كان MCID (معرف محتوى العلامة) لـ BDC هو 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // تخزين BDC للاستخدام لاحقًا.
            }
        }
    }

    // التحقق مما إذا كان المشغل عبارة عن مثيل لـ Do (رسم الكائن).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // تحويل المشغل إلى نوع Do.
        if (doXobj != null)
        {
            // إنشاء BDC جديد للصورة وإدخاله في محتويات الصفحة.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // الإدراج قبل المشغل الحالي.
            i++; // زيادة الفهرس لاستيعاب BDC المدخل.
            page.getContents().insert(i + 1, new EMC()); // إدراج EMC (نهاية محتوى العلامة).
            i++; // زيادة الفهرس مرة أخرى.
        }
    }

    // التحقق مما إذا كان المشغل عبارة عن مثيل لـ TextShowOperator (لعرض النص).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // تحويل المشغل إلى نوع TextShowOperator.
        if (tx != null)
        {
            // التحقق من محتوى نصي محدد وإدخال BDC المقابلة.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // الإدراج قبل المشغل الحالي.
                i++; // زيادة الفهرس.
                page.getContents().insert(i + 1, new EMC()); // إدراج EMC.
                i++; // زيادة الفهرس.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // الإدراج قبل المشغل الحالي.
                i++; // زيادة الفهرس.
                page.getContents().insert(i + 1, new EMC()); // إدراج EMC.
                i++; // زيادة الفهرس.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // الإدراج قبل المشغل الحالي.
                i++; // زيادة الفهرس.
                page.getContents().insert(i + 1, new EMC()); // إدراج EMC.
                i++; // زيادة الفهرس.
            }
        }
    }
}
 
    // استرجاع المحتوى الموسوم من المستند.
    ITaggedContent tagged = document.getTaggedContent();

    // معالجة المحتوى الموسوم لتعديل سمات الهيكل.
    // الحصول على العنصر الفرعي الأول من العنصر الجذري في المحتوى الموسوم.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // مسح العناصر الفرعية الحالية.

    // وضع علامة على helloBdc مع عنصر هيكل الأب.
    MCRElement mcr = p.tag(helloBdc);

    // إنشاء وتعيين سمات الهيكل للعنصر الموسوم.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // تعيين مساحة بعد السمة.
    attrs.setAttribute(attr); // تطبيق السمة على الهيكل.

    // إنشاء عنصر جديد من نوع FigureElement في المحتوى الموسوم.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // إدراج عنصر الشكل في الموقع الثاني.
    figure.setAlternativeText("A fly."); // تعيين نص بديل للشكل.

    // وضع علامة على imageBdc مع عنصر الشكل.
    MCRElement mcr = figure.tag(imageBdc);

    // استرجاع عنصر الهيكل الأب للـ MCR (مرجع المحتوى الموسوم) المحدد
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // إنشاء سمة هيكلية جديدة للمساحة بعد العنصر
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // تعيين قيمة المساحة بعد إلى 3.625 وحدة
    attrs.setAttribute(spaceAfter); // تعيين السمة المساحية بعد إلى سمات الهيكل

    // إنشاء سمة هيكلية جديدة للصندوق المحيط (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // تعيين القيم للصندوق المحيط للسمة الهيكلية
    attrs.setAttribute(bbox); // تعيين السمة المحيطة إلى سمات الهيكل

    // إنشاء سمة هيكلية جديدة للتخطيط
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // تعيين نوع التخطيط إلى بلوك
    attrs.setAttribute(placement); // تعيين سمة التخطيط إلى سمات الهيكل

    // استرجاع العنصر الفرعي الرابع من العنصر الجذري للهيكل الموسوم
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // مسح أي عناصر فرعية موجودة من p2

    // إنشاء عنصر SpanElement جديد ليضاف إلى p2
    SpanElement span1 = tagged.createSpanElement();

    // إنشاء سمات هيكلية لعنصر السبن
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // إنشاء سمة هيكلية جديدة لنوع زخرفة النص
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // تعيين زخرفة النص إلى تسطير
    attrs.setAttribute(textDecorationType); // تعيين سمة نوع زخرفة النص إلى سمات الهيكل

    // إنشاء سمة هيكلية جديدة لسماكة زخرفة النص
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // تعيين سماكة زخرفة النص إلى 0
    attrs.setAttribute(textDecorationThickness); // تعيين سمة سماكة زخرفة النص إلى سمات الهيكل

    // إنشاء سمة هيكلية جديدة للون زخرفة النص
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // تعيين قيم اللون RGB لزخرفة النص
    attrs.setAttribute(textDecorationColor); // تعيين سمة لون زخرفة النص إلى سمات الهيكل

    p2.appendChild(span1); // إضافة عنصر span1 إلى p2


    // إنشاء عنصر MCR جديد وتوسيمه مع pBdc
    MCRElement mcr = p2.tag(pBdc);
    // استرجاع عنصر الهيكل الأب لـ MCR وإنشاء سمات التخطيط
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // إنشاء سمة هيكلية جديدة لمحاذاة النص
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // تعيين محاذاة النص إلى المركز
    attrs.setAttribute(textAlign); // تعيين سمة محاذاة النص إلى سمات الهيكل

    // إنشاء سمة هيكلية جديدة للمساحة بعد العنصر
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // تعيين قيمة المساحة بعد إلى 21.75 وحدة
    attrs.setAttribute(spaceAfter); // تعيين السمة المساحية بعد إلى سمات الهيكل


    // إنشاء عنصر SpanElement جديد ليضاف إلى p2
    SpanElement span2 = tagged.createSpanElement();

    // إنشاء سمات هيكلية لعنصر السبن
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // إنشاء سمة هيكلية جديدة لنوع زخرفة النص
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // تعيين زخرفة النص إلى تسطير
    attrs.setAttribute(textDecorationType); // تعيين سمة نوع زخرفة النص إلى سمات الهيكل

    // إنشاء سمة هيكلية جديدة للون زخرفة النص باستخدام المفتاح المحدد.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // تعيين قيمة رقمية للمصفوفة لسمة لون زخرفة النص.
    // اللون ممثل في مصفوفة من قيم RGB، حيث كل قيمة هي من نوع Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // المكون الأحمر
    new Double[] { (0.384308) },  // المكون الأخضر
    new Double[] { (0.756866) }   // المكون الأزرق
    });

    // تعيين سمة لون زخرفة النص إلى كائن attrs.
    attrs.setAttribute(textDecorationColor);

    // إضافة عنصر span الفرعي إلى العنصر الأب p2.
    p2.appendChild(span2);

    // إنشاء مثيل جديد لـ LinkElement للرابط الثاني.
    LinkElement link2 = tagged.createLinkElement();

    // تعيين معرف فريد للعنصر الرابط باستخدام UUID مولد عشوائيًا.
    link2.setId(UUID.randomUUID().toString());

    // إضافة عنصر link2 كفرعي لـ span2.
    span2.appendChild(link2);

    // توسييم عنصر link2 مع التعليق التوضيحي المقابل من تعليقات الصفحة.
    link2.tag(page.getAnnotations().get_Item(1));

    // توسييم عنصر link2 مع معلومات تعريف أو سياق إضافي (link2Bdc).
    link2.tag(link2Bdc);

    // إنشاء مثيل آخر لـ LinkElement للرابط الأول.
    LinkElement link1 = tagged.createLinkElement();

    // تعيين معرف فريد للعنصر link1 باستخدام UUID مولد عشوائيًا.
    link1.setId(UUID.randomUUID().toString());

    // إضافة عنصر link1 كفرعي لـ span1.
    span1.appendChild(link1);

    // توسييم عنصر link1 مع التعليق التوضيحي المقابل من تعليقات الصفحة.
    link1.tag(page.getAnnotations().get_Item(2));

    // توسييم عنصر link1 مع معلومات تعريف أو سياق إضافي (link1Bdc).
    link1.tag(link1Bdc);

    // إزالة العنصر الفرعي الأول من العنصر الجذري للمستند الموسوم.
    tagged.getRootElement().removeChild(0);

    // حفظ المستند إلى الدليل المحدد مع اسم الملف "_out.pdf".
    document.save(dataDir + "_out.pdf");

```


## ما الجديد في Aspose.PDF 24.6

منذ الإصدار 24.6، أصبح Aspose.PDF لجافا يسمح بتوقيع PDF باستخدام java.security.cert.X509Certificate وjava.security.PrivateKey:

يقوم هذا الكود باسترجاع شهادة ومفتاح خاص من مخزن الشهادات، ثم يستخدمهما لتطبيق توقيع رقمي على الصفحة الأولى من مستند PDF.

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## ما الجديد في Aspose.PDF 24.5

منذ إصدار 24.5، تم تنفيذ مكونات إضافية لمحرر النماذج.

**كيفية تحرير النماذج في PDF باستخدام محرر النماذج**

- قم بتعيين مفاتيح الترخيص الخاصة بك
- قم بإنشاء مثيل لفئة FormEditor، التي توفر طرقًا للتلاعب بنماذج PDF
- قم بإنشاء مثيل لفئة FormEditorAddOptions، التي تحدد الخيارات لإضافة حقول النموذج إلى مستند PDF
- أضف مصدر ملف إدخال ومصدر ملف إخراج إلى كائن FormEditorAddOptions، باستخدام فئة FileDataSource التي تمثل مسار ملف أو دفق
- استدع طريقة Process لكائن FormEditor، بتمرير كائن FormEditorAddOptions كمعامل
- قم بالوصول إلى النتيجة باستخدام ResultContainer.resultCollection

```java

    // تحديد مسارات الإدخال والإخراج لملفات PDF.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // قم بإنشاء مثيل لمكون إضافي لمحرر النماذج.
    FormEditor pdfFormPlugin = new FormEditor();

    // إنشاء خيارات لإضافة حقول النموذج.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // إنشاء حقل نموذج مربع نص.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // إنشاء حقل نموذج مربع تحرير وسرد.
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // إنشاء حقل نموذج مربع اختيار.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // إنشاء حقل نموذج مربع اختيار.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // إنشاء حقل نموذج مربع اختيار.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // إضافة ملفات الإدخال والإخراج إلى الخيارات.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // معالجة حقول النموذج باستخدام المكون الإضافي.
    ResultContainer results = pdfFormPlugin.process(opt);
```


يتيح هذا الإصدار لنا العمل مع طبقات PDF. على سبيل المثال:

- قفل طبقة PDF
- استخراج عناصر طبقة PDF
- تسطيح PDF متعدد الطبقات
- دمج جميع الطبقات داخل PDF في واحدة

**قفل طبقة PDF**

منذ إصدار 24.5، يمكنك فتح ملف PDF، وقفل طبقة معينة في الصفحة الأولى، وحفظ المستند بالتغييرات. تم إضافة طريقتين جديدتين وخاصية واحدة:

Layer.Lock(); - يقفل الطبقة.
Layer.Unlock(); - يفتح الطبقة.
Layer.Locked; - خاصية تشير إلى حالة قفل الطبقة.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**استخراج عناصر طبقة PDF**

تسمح مكتبة Aspose.PDF for Java باستخراج كل طبقة من الصفحة الأولى وحفظ كل طبقة في ملف منفصل.

لإنشاء ملف PDF جديد من طبقة، يمكن استخدام الكود التالي:

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**تسطيح PDF ذو الطبقات**

تفتح مكتبة Aspose.PDF لـ Java ملف PDF، وتقوم بالمرور عبر كل طبقة في الصفحة الأولى، وتسطيح كل طبقة، مما يجعلها دائمة على الصفحة.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

تقبل طريقة Layer.flatten(boolean cleanupContentStream) الوسيط البولياني الذي يحدد ما إذا كان سيتم إزالة علامات مجموعة المحتوى الاختياري من دفق المحتوى.
تعيين الوسيط cleanupContentStream إلى false يسرع عملية التسطيح.

**دمج جميع الطبقات داخل PDF في واحدة**

تسمح مكتبة Aspose.PDF لـ Java بدمج إما جميع طبقات PDF أو طبقة معينة في الصفحة الأولى في طبقة جديدة وحفظ المستند المحدث.

تمت إضافة طريقتين لدمج جميع الطبقات في الصفحة:

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

المعلمة الثانية تسمح بإعادة تسمية علامة مجموعة المحتوى الاختياري. القيمة الافتراضية هي "oc1" (/OC /oc1 BDC).

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // أو page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## ما الجديد في Aspose.PDF 24.4

هذا الإصدار قدم إضافات جافا لـ PDF:

- إضافة تسطيح النماذج

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // تحقق من النتيجة.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- مصدر النماذج

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // استخدام الإضافة.
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // تحقق من النتيجة.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- دمج البرنامج المساعد

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- البرنامج المساعد للمحسن

كيفية تقليل حجم مستندات PDF؟

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

كيفية تغيير حجم مستندات PDF؟

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


كيف يتم تدوير مستندات PDF؟

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## ما الجديد في Aspose.PDF 24.3

من الإصدار 24.3 يتم تنفيذ البحث من خلال قائمة من العبارات في TextFragmentAbsorber.

```java

    String[] expressions = new String[] {
      //الكشف عن رقم الهاتف
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //الكشف عن رقم البطاقة
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


الميزة التالية هي إضافة القدرة على تحويل الجداول لمحول PDF إلى Markdown

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## ما الجديد في Aspose.PDF 24.2

من الإصدار 24.2 أصبح من الممكن إضافة العلامة المائية في PDF مع AcroForms. يعتبر TextStamp مناسباً للاستخدام مع ملفات AcroForm. إذا كنت تستخدم TextStamp للملفات XFA، يتم رسم النص على الصفحة كما في ملف PDF العادي (يمكن رؤيته في عارضات PDF التي لا تستطيع قراءة ملفات XFA، على سبيل المثال، في متصفح Chrome). لإضافة نص إلى ملف XFA، يجب تغييره في XML الداخلي لملف XFA.

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sample Stamp</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


Set StateModel for Annotation  
يمكننا استخدام setReviewState و setMarkedState من فئة MarkupAnnotation لتعيين الحالة المطلوبة.  
تحتوي جميع التعليقات التوضيحية للعلامات على خيار تعيين الحالة المتاح.

```java

    // فتح مستند PDF المصدر
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // إنشاء تعليق توضيحي
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    // تعيين عنوان التعليق التوضيحي
    textAnnotation.setTitle("عنوان تعليق توضيحي للعينة");

    // تعيين موضوع التعليق التوضيحي
    textAnnotation.setSubject("موضوع العينة");
    // تحديد محتويات التعليق التوضيحي
    textAnnotation.setContents("محتويات العينة للتعليق التوضيحي");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    // إضافة التعليق التوضيحي في مجموعة التعليقات التوضيحية للصفحة
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    // حفظ ملف الإخراج
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


من 24.2 تنفيذ تحويل OFD إلى PDF:

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## ما الجديد في Aspose.PDF 24.1

من إصدار 24.1 تنفيذ تحويل PDF إلى Markdown:

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

أيضًا، في 24.1 تم تنفيذ مقاطعة الخيط باستخدام InterruptMonitor.

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");

          //تحويل عبارات foreach إلى while
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("text");
          row2.getCells().add("text");
          row2.getCells().add("text");
          String LongText = "لوريم إيبسوم دولار سيت أميت، كونسيكتيتور أديبيسسينغ إيليت. أينيان كومودو ليغولا إيغيت دولار. أينيان ماسا. كوم سوسيس ناتوكي بيناتيبوس إيت ماجنس ديس بارتوريانت مونتيس، ناسيتيور ريديكولوس موس. دونك كوام فيليس، ألتريسيز نيك، بيناتيسكيو إي، بريتيوم كويز، سيم. نولا كونسكات ماسا كويز إينيم. دونك بيد جاستو، فرينجيلا فيل، أليكويت نيك، فولبوتاتي إيغيت، أركو. إن إينيم جاستو، رونكوس أوت، إمبيردييت أ، فينانتيس فيتاي، جاستو. نولام ديكتوم فيليس يو بيد موليس بريتيوم. إنتيجر تينكيدونت. كراس دابيبوس. فيفاموس إليمنتوم سيمبير نيسي. أينيان فولبوتاتي إليفند تيلوس.";
          row2.getCells().add(LongText);
          row2.getCells().add("text");
          row2.getCells().add("text");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Interrupting the save thread at " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("Process is started thread at " + System.currentTimeMillis());

    // يجب أن يكون المهلة أقل من الوقت المطلوب لحفظ المستند بالكامل (بدون مقاطعة).
    Thread.sleep(500);

    // مقاطعة العملية
    monitor.interrupt();

    System.out.println("Interrupted the save thread at " + System.currentTimeMillis());
```


## ما الجديد في Aspose.PDF 23.12

يمكن العثور على النموذج واستبدال النص باستخدام جزء الكود التالي:

```java

    Document document = new Document(input);
    String expectedText = "This is a text added while creating new PDF in Kofx Power PDF Standard.";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```            

أو، يمكن إزالة النموذج بالكامل:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    // تحويل جمل foreach إلى while
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```


إزالة النموذج بطريقة أخرى:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
``` 

- يمكن حذف جميع النماذج باستخدام المقتطف البرمجي التالي:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## ما الجديد في Aspose.PDF 23.11

من هذا الإصدار أصبح بالإمكان إزالة النصوص المخفية من ملف PDF:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    // تحويل عبارات foreach إلى while
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## ما الجديد في Aspose.PDF 23.10

يقدم التحديث الحالي ثلاث طرق لإزالة العلامات من ملفات PDF ذات العلامات.

- إزالة بعض عناصر العقدة من documentElement (عنصر الشجرة الجذر):

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // يمكنك أيضًا حذف structElement نفسه
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- إزالة جميع علامات العناصر المعلمة من المستند، ولكن الاحتفاظ بعناصر الهيكل:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- إزالة العلامات تمامًا:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

لقد قمنا بتنفيذ ميزة جديدة لقياس ارتفاع الحرف. استخدم الكود التالي لقياس ارتفاع الحرف:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

لاحظ أن القياس يعتمد على الخط المضمن في المستند. إذا كانت أي معلومات لأبعاد مفقودة، فإن هذه الطريقة تعيد 0.

## ما الجديد في Aspose.PDF 23.9

بدءًا من 23.9 يتم دعم إزالة التعليق الفرعي من حقل قابل للتعبئة.

المثال 1:

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "الخيار 1";
    String option2 = "الخيار 2";
    String outputPdf = "output.pdf";

    final Document document = new Document();
    try /*JAVA: كان يستخدم*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // تعيين قيمة خيار مجموعة مربعات الاختيار الأول
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


إضافة صورة باستخدام ImageFilterType.Flate لا يحافظ على الشفافية.

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## ما الجديد في Aspose.PDF 23.8

تمت إضافة وظيفة لاكتشاف التحديثات المتزايدة في مستند PDF في الإصدار 23.8. تعيد هذه الوظيفة 'true' إذا تم حفظ المستند بتحديثات متزايدة، وإلا فإنها تعيد 'false'.

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```    

ميزة أخرى هي نسخ OutputIntents من PDF المدخل إلى PDF الوجهة

نضيف خاصية عامة جديدة Document.getOutputIntents() للسماح بالوصول إلى النوايا الناتجة في المستند. في الوقت الحالي، يتم دعم استخدام النوايا الناتجة الموجودة بالفعل في بعض المستندات، ولا يمكن للمستخدم إنشاء OutputIntent من البداية.

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


من دعم Aspose.PDF 23.8 لإضافة استخراج الأشكال:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    // تحويل عبارات foreach إلى while
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // إعادة حساب موقع جديد نظرًا لاختلاف حجم الصفحة في ملف PDF الأصلي
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


يدعم أيضًا القدرة على اكتشاف التجاوز عند إضافة النص:

```java

    Document doc = new Document();
    String paragraphContent = "لوريم إيبسوم دولار سيت أميت، كونسيكتيتور أديبيسيسينغ إليت. كراس نيسل تورتور، إفيسيتيور سيد كورسوس إن، لوبورتيز فيتاي نولا. كويزك رونكوس، فيليس سيد ديكتوم سيمبر، إست تيلوس فينيبوس أوغوي، أوت فيويغات إينيم ريسوس إيجيت تورتور. نولا فينيبوس فيليت نيك أنتي غرافيذا سوليكيتودين. موربي سوليكيتودين فيهيكولا فاسيليسيس. فيستيبيولوم أك كونفاليس إيرات. أوت إيجيت فارياس سيم. نام فارياس فاريترا لوريم، آيد أولامكوربر جوستو أوكتور أك. إنتيجر كويز إيرات فيتاي لاكوس موليس فولبوتات إيجيت إت إيروس. دونك أك إفيسيتيور دولار. مايكيناس نون دابيبيس نيسي، أوت بيلينتيسكوي إليت. سيد بيلينتيسكوي رونكوس أنتي، أك كونسيكتيتور ليغولا فيفيرا فيل. إنتيجر إيجيت بيبيندوم أنتي. بيلينتيسكوي هابيتانت موربي تريستيك سينيكتوس إت نيتوس إت ماليسوادا فاميس أك توربيس إيغستاس. كوريبيتور إليمنتوم، سيم أك أوكتور فولبوتات، أنتي ليبرو إياكوليس دولار، فيتاي فاسيليسيس دولار لوريم آت أورسي. سيد لوريت دوي آيد نيسي أكومسان، آيد بوسوير ديا أكومسان.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## ما الجديد في Aspose.PDF 23.7

من الإصدار 23.7 تم دعم إعدادات حوار الطباعة لتوسيع الصفحة:

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## ما الجديد في Aspose.PDF 23.6

من الإصدار 23.6 تم دعم إضافة القدرة على تعيين عنوان صفحة HTML، Epub.

كود لـ HTML:

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NEW PAGE & TITILE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


code for EPUB:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>صفحة جديدة وعنوان</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

من الإصدار 23.6 دعم لتوفير API لتحديد موضع الرسومات المتجهة:

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## ما الجديد في Aspose.PDF 23.1

من الإصدار 23.1 تم دعم إنشاء تعليق PrinterMark. تمت إضافة أحد أنواع التعليقات: ColorBarAnnotation.

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## ما الجديد في Aspose.PDF 22.12

من هذا الإصدار تم دعم تحويل PDF إلى صورة DICOM:

```java
    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## ما الجديد في Aspose.PDF 22.9

من الإصدار 22.09 دعم إضافة خاصية لتعديل ترتيب مواضيع الشهادات (E=، CN=، O=، OU=،) في التوقيع.

```java
    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance( new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## ما الجديد في Aspose.PDF 22.8

من Aspose.PDF 23.8 دعم لإضافة طريقة لإعادة بناء جدول xref:

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```

## ما الجديد في Aspose.PDF 22.6

PDF إلى PDF_A_1A - تنفيذ خيار لإزالة لون الشفافية لتجنب حجم ملف الإخراج الكبير.

من الإصدار 22.5 العميل قادر على التحكم في جودة الشفافية المحولة، وحجم ملف الإخراج كنتيجة:

```java
    opts.setTransparencyResolution(300);
```

## ما الجديد في Aspose.PDF 22.5

أثناء تحويل PDF/A يتم إزالة المحتوى الشفاف واستبداله بصورة.
لقد قمنا بتنفيذ ميزة جديدة، والآن يمكن للعميل التحكم في جودة الصورة باستخدام المعامل TransparencyResolution:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## ما الجديد في Aspose.PDF 22.4

يتضمن هذا الإصدار معلومات لـ Aspose.PDF for Java:

- PDF إلى ODS: التعرف على النص في الكتابة الفوقية والكتابة السفلية؛

**مثال**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF إلى XMLSpreadSheet2003: التعرف على النص في الكتابة الفوقية والكتابة السفلية؛

- PDF إلى Excel: التعرف على النص في الكتابة الفوقية والكتابة السفلية؛

## ما الجديد في Aspose.PDF 22.3

PDF إلى ODS: الدعم للكتابة من اليمين لليسار متاح في الإصدار 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## ما الجديد في Aspose.PDF 22.2

يتضمن هذا الإصدار PDF إلى XSLX: الدعم للكتابة من اليمين لليسار (العبرية، العربية).

## ما الجديد في Aspose.PDF 22.1

Aspose.PDF for Java يسمح بتحميل مستندات Portable Document Format (PDF) الإصدار 2.0.

## ما الجديد في Aspose.PDF 21.10

### كيفية اكتشاف النص المخفي؟

يرجى استخدام الكود التالي:

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## ما الجديد في Aspose.PDF 21.8

### كيفية تغيير لون النص في التوقيع الرقمي؟

في الإصدار 21.8 يسمح setForegroundColor بتغيير لون النص في التوقيع الرقمي:

```java
يرجى استخدام الكود التالي:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    //إنشاء مستطيل لموقع التوقيع
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
//تعيين لون النص
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // توقيع ملف PDF
                    pdfSign.sign(1, true, rect, pkcs);
                    //حفظ ملف PDF الناتج
                    pdfSign.save(outFile);
```

## ما الجديد في Aspose.PDF 21.6

### إخفاء الصورة باستخدام ImagePlacementAbsorber من المستند

مع Aspose.PDF لـ Java يمكنك إخفاء الصور باستخدام ImagePlacementAbsorber من المستند:

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## ما الجديد في Aspose.PDF 21.5

### إضافة API لدمج الصور

Aspose.PDF 21.4 يتيح لك دمج الصور. يدمج قائمة تدفقات الصور كتيار صورة واحد. يتم دعم تنسيقات المخرجات Png/jpg/tiff، في حالة استخدام تنسيق غير مدعوم يتم ترميز تيار المخرجات كـ Jpeg افتراضيًا. اتبع الكود التالي:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


أيضًا يمكنك دمج صورك بتنسيق Tiff:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## ما الجديد في Aspose.PDF 21.02

Aspose.PDF v21.02 توقيع PDF بتوقيعات PAdES LTV

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //توقيع PDF بتوقيعات PAdES LTV
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```