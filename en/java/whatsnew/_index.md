---
title: What's new 
linktitle: What's new
type: docs
weight: 10
url: /java/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for Java that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
TechArticle: true 
AlternativeHeadline: Popular New Features in Aspose.PDF for Java
Abstract: The What’s New section of the Aspose.PDF for Java documentation provides an overview of the latest updates, enhancements, and bug fixes introduced in recent releases. It highlights new features, performance improvements, and compatibility updates to help developers stay informed about the latest advancements in PDF processing. The documentation also includes details on deprecated functionalities and recommended alternatives. By regularly reviewing this section, developers can ensure they are utilizing the most efficient and up-to-date features in their Java applications for seamless PDF management.
SoftwareApplication: java
---

## What's new in Aspose.PDF 24.8

Since 24.8, support for the PDF/A-4 format:

```java

    Document document = new Document(inputPdf);
    // Only PDF-2.x documents can be converted to PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

Also, is it possible to add alternative text for the Image Stamp:

The AlternativeText property has been added to ImageStamp - if a value is assigned to it, then when adding an ImageStamp to a document it has Alternative Text.

```java

    String p1_Alt1 = "*** page 1, Alt text 1 ***",
                    p1_Alt2 = "*** page 1, Alt text 2 ***",
                    p2_Alt1 = "--- page 1, Alt text 1 ---",
                    p2_Alt2 = "--- page 1, Alt text 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // To page 1
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // To page 2
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

    // Save document
    document.save(outFile);
```

Also, the following code shows how to add AlternativeText in the existing images in FigureElements.

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

            // Set Alternative Text
            figureElement.setAlternativeText("Figure alternative text (technique 1)");
        }
    }

    // Save document
    document.save(outFile);
```

## What's new in Aspose.PDF 24.7

Since the 24.7 release, as part of the editing tagged PDF, were added methods on **Aspose.Pdf.LogicalStructure.Element**:

- Tag (add tags to specific operators like images, text, and links)
- InsertChild
- RemoveChild
- ClearChilds

These methods allow you to edit PDF file tags, for example:

```java

    Document document = new Document(dataDir + "test.pdf");

    // Retrieve the first page of the document.
    Page page = document.getPages().get_Item(1);

    // Initialize variables to hold BDC (Begin Dictionary Context) elements for different purposes.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // Iterate through the contents of the page.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // Get the current operator from the page contents.
        Operator op = page.getContents().get_Item(i);

        // Check if the operator is an instance of BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // Cast the operator to BDC type.
        if (bdc != null)
        {
            // Check if the MCID (Mark Content Identifier) of the BDC is 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // Store the BDC for later use.
            }
        }
    }

    // Check if the operator is an instance of Do (Draw Object).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // Cast the operator to Do type.
        if (doXobj != null)
        {
            // Create a new BDC for an image and insert it into the page contents.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // Insert before the current operator.
            i++; // Increment the index to account for the inserted BDC.
            page.getContents().insert(i + 1, new EMC()); // Insert an EMC (End Mark Content).
            i++; // Increment the index again.
        }
    }

    // Check if the operator is an instance of TextShowOperator (for text display).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // Cast the operator to TextShowOperator type.
        if (tx != null)
        {
            // Check for specific text content and insert corresponding BDCs.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // Insert before the current operator.
                i++; // Increment the index.
                page.getContents().insert(i + 1, new EMC()); // Insert an EMC.
                i++; // Increment the index.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // Insert before the current operator.
                i++; // Increment the index.
                page.getContents().insert(i + 1, new EMC()); // Insert an EMC.
                i++; // Increment the index.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // Insert before the current operator.
                i++; // Increment the index.
                page.getContents().insert(i + 1, new EMC()); // Insert an EMC.
                i++; // Increment the index.
            }
        }
    }
}
 
    // Retrieve the tagged content from the document.
    ITaggedContent tagged = document.getTaggedContent();

    // Process the tagged content to modify structure attributes.
    // Get the first child element of the root element in the tagged content.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // Clear existing child elements.

    // Tag the helloBdc with the parent structure element.
    MCRElement mcr = p.tag(helloBdc);

    // Create and set structure attributes for the tagged element.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Set space after attribute.
    attrs.setAttribute(attr); // Apply the attribute to the structure.

    // Create  a new FigureElement in the tagged content.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // Insert the figure element at the second position.
    figure.setAlternativeText("A fly."); // Set alternative text for the figure.

    // Tag the imageBdc with the figure element.
    MCRElement mcr = figure.tag(imageBdc);

    // Retrieve the parent structure element of the specified MCR (Marked Content Reference)
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for space after the element
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // Set the space after value to 3.625 units
    attrs.setAttribute(spaceAfter); // Assign the space after attribute to the structure attributes

    // Create a new StructureAttribute for bounding box (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // Set the bounding box values for the structure attribute
    attrs.setAttribute(bbox); // Assign the bounding box attribute to the structure attributes

    // Create a new StructureAttribute for placement
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // Set the placement type to block
    attrs.setAttribute(placement); // Assign the placement attribute to the structure attributes

    // Retrieve the fourth child element from the root element of the tagged structure
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // Clear any existing child elements from p2

    // Create a new SpanElement to be added to p2
    SpanElement span1 = tagged.createSpanElement();

    // Create structure attributes for the span element
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for text decoration type
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Set text decoration to underline
    attrs.setAttribute(textDecorationType); // Assign the text decoration type attribute to the structure attributes

    // Create a new StructureAttribute for text decoration thickness
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // Set the thickness of the text decoration to 0
    attrs.setAttribute(textDecorationThickness); // Assign the text decoration thickness attribute to the structure attributes

    // Create a new StructureAttribute for text decoration color
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // Set the RGB color values for the text decoration
    attrs.setAttribute(textDecorationColor); // Assign the text decoration color attribute to the structure attributes

    p2.appendChild(span1); // Append the span1 element to p2


    // Create a new MCR element and tag it with pBdc
    MCRElement mcr = p2.tag(pBdc);
    // Retrieve the parent structure element of the MCR and create layout attributes
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for text alignment
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // Set text alignment to center
    attrs.setAttribute(textAlign); // Assign the text alignment attribute to the structure attributes

    // Create a new StructureAttribute for space after the element
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // Set the space after value to 21.75 units
    attrs.setAttribute(spaceAfter); // Assign the space after attribute to the structure attributes


    // Create a new SpanElement to be added to p2
    SpanElement span2 = tagged.createSpanElement();

    // Create structure attributes for the span element
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Create a new StructureAttribute for text decoration type
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Set text decoration to underline
    attrs.setAttribute(textDecorationType); // Assign the text decoration type attribute to the structure attributes

    // Create a new StructureAttribute for text decoration color using the specified key.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // Set the array number value for the text decoration color attribute.
    // The color is represented in an array of RGB values, where each value is a Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // Red component
    new Double[] { (0.384308) },  // Green component
    new Double[] { (0.756866) }   // Blue component
    });

    // Set the text decoration color attribute to the attrs object.
    attrs.setAttribute(textDecorationColor);

    // Append a child span element to the parent element p2.
    p2.appendChild(span2);

    // Create a new LinkElement instance for the second link.
    LinkElement link2 = tagged.createLinkElement();

    // Assign a unique ID to the link element using a randomly generated UUID.
    link2.setId(UUID.randomUUID().toString());

    // Append the link2 element as a child of span2.
    span2.appendChild(link2);

    // Tag the link2 element with the corresponding annotation from the page's annotations.
    link2.tag(page.getAnnotations().get_Item(1));

    // Tag the link2 element with additional metadata or context (link2Bdc).
    link2.tag(link2Bdc);

    // Create another LinkElement instance for the first link.
    LinkElement link1 = tagged.createLinkElement();

    // Assign a unique ID to the link1 element using a randomly generated UUID.
    link1.setId(UUID.randomUUID().toString());

    // Append the link1 element as a child of span1.
    span1.appendChild(link1);

    // Tag the link1 element with the corresponding annotation from the page's annotations.
    link1.tag(page.getAnnotations().get_Item(2));

    // Tag the link1 element with additional metadata or context (link1Bdc).
    link1.tag(link1Bdc);

    // Remove the first child element from the root element of the tagged document.
    tagged.getRootElement().removeChild(0);

    // Save the document to the specified output directory with the filename "_out.pdf".
    document.save(dataDir + "_out.pdf");

```

## What's new in Aspose.PDF 24.6

Since 24.6 Aspose.PDF for Java allows to sign PDF with java.security.cert.X509Certificate, java.security.PrivateKey:

This code retrieves a certificate and private key from the certificate store and then uses them to apply a digital signature to the first page of a PDF document. 

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

## What's new in Aspose.PDF 24.5

Since the 24.5 release, the Form Editor Plugins implemented.

**How to Edit Forms in PDF using Form Editor**

- Set your license keys
- Create an instance of the FormEditor class, which provides methods for manipulating PDF forms
- Create an instance of the FormEditorAddOptions class, which specifies the options for adding form fields to a PDF document
- Add an input file source and an output file source to the FormEditorAddOptions object, using the FileDataSource class which represents a file path or stream
- Call the Process method of the FormEditor object, passing the FormEditorAddOptions object as a parameter
- Access the result using ResultContainer.resultCollection

```java

    // Specify the input and output paths for the PDF files.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // Create an instance of the FormEditor plugin.
    FormEditor pdfFormPlugin = new FormEditor();

    // Create options for adding form fields.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // Create a textbox form field.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // Create a combo box form field.
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

    // Create a checkbox form field.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // Create a checkbox form field.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // Create a checkbox form field.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // Add input and output files to the options.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // Process the form fields using the plugin.
    ResultContainer results = pdfFormPlugin.process(opt);
```

This release allows us to work with PDF layers. For example:

- lock a PDF layer
- extract PDF layer elements
- flatten a layered PDF
- merge All Layers inside the PDF into one

**Lock a PDF layer**

Since the 24.5 release, you can open a PDF, lock a specific layer on the first page, and save the document with the changes. There are two new methods and one property was added:

Layer.Lock(); -  Locks the layer.
Layer.Unlock(); - Unlocks the layer.
Layer.Locked; - Property, indicating the layer locked state.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**Extract PDF layer elements**

The Aspose.PDF for Java library allows extracts of each layer from the first page and saves each layer to a separate file.

To create a new PDF from a layer, the following code snippet can be used:

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```

**Flatten a layered PDF**

Aspose.PDF for Java library opens a PDF, iterates through each layer on the first page, and flattens each layer, making it permanent on the page.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

The Layer.flatten(boolean cleanupContentStream) method accepts the boolean parameter that specifies whether to remove optional content group markers from the content stream.
Setting the cleanupContentStream parameter to false speeds up the process of flattening.

**Merge All Layers inside the PDF into one**

The Aspose.PDF for Java library allows merges either all PDF layers or a specific layer on the first page into a new layer and saves the updated document.

Two methods were added to merge all layers on the page:

- void mergeLayers(String newLayerName);
- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

The second parameter allows renaming the optional content group marker. The default value is "oc1" (/OC /oc1 BDC).

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // Or page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## What's new in Aspose.PDF 24.4

This release introduced Java plugins for PDF:

- Form Flattener Plugin

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // Check result.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- Form Exporter

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // Plugin use.
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

    // Check result.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```

- Merger Plugin

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

- Optimizer Plugin

How to reduce size of PDF Documents?

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

How to resize PDF Documents?

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

How to rotate PDF Documents?

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

## What's new in Aspose.PDF 24.3

From 24.3 implement a search through a list of phrases in a TextFragmentAbsorber.

```java

    String[] expressions = new String[] {
      //detect phone number
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //detect card number
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

Next feature is adding  the ability to convert tables for the PDF to Markdown converter

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## What's new in Aspose.PDF 24.2

From 24.2 possible to add the Watermark in PDF with AcroForms. TextStamp is suitable for use with AcroForm files. If you use TextStamp for XFA files, the text is drawn on the page as in a usual PDF file (it can be seen in those PDF viewers that cannot read XFA files, for example, in a Chrome browser). To add text to the XFA file, it must be changed in the XFA file's internal XML.

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
We can use setReviewState and setMarkedState from MarkupAnnotation class to set needed state.
All markup annotations have a Set State option available.

```java

    // Open the source PDF document
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // Create annotation
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    //Set annotation title
    textAnnotation.setTitle("Sample Annotation Title");

    //Set annotation subject
    textAnnotation.setSubject("Sample Subject");
    //Specify the annotation contents
    textAnnotation.setContents("Sample contents for the annotation");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    //Add annotation in the annotations collection of the page
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    //Save the output file
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```

From 24.2 implement OFD to PDF conversion:

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## What's new in Aspose.PDF 24.1

From 24.1 release implement PDF to Markdown conversion:

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

Also, in 24.1 thread interruption using the InterruptMonitor has been implemented.

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

          //foreach to while statements conversion
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
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
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

    // The timeout should be less than the time required for full document save (without interruption).
    Thread.sleep(500);

    // Interrupt the process
    monitor.interrupt();

    System.out.println("Interrupted the save thread at " + System.currentTimeMillis());
```

## What's new in Aspose.PDF 23.12

The form can be found and the text can be replaced using the following code snippet:

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

Or, the form can be completely removed:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    //foreach to while statements conversion
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

Another variant of removing the form:

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

- All forms can be deleted using the following code snippet:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## What's new in Aspose.PDF 23.11

From this release possible to remove hidden text from PDF file:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    //foreach to while statements conversion
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

## What's new in Aspose.PDF 23.10

The current update presents three versions of Removing tags from tagged PDFs.

- Remove some node element from a documentElement (root tree element):

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // You can also delete the structElement itself
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- Remove all marked elements tags from the document, but keep the structure elements:

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

- Remove tags at all:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

We've implemented a new feature to measure character height. Use the following code to measure the height of a character:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

Note that the measurement is based on the font embedded in the document. If any information for a dimension is missing, this method returns 0.

## What's new in Aspose.PDF 23.9

From 23.9 support to remove a child annotation from a fillable field.

example 1:

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
    String option1 = "option 1";
    String option2 = "option 2";
    String outputPdf = "output.pdf";

    final Document document = new Document();
    try /*JAVA: was using*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // Set the first checkbox group option value
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

Adding image with ImageFilterType.Flate does not preserve transparency.

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

## What's new in Aspose.PDF 23.8

The function for detecting Incremental Updates in a PDF document has been added in 23.8. This function returns 'true' where document was saved with incremental updates, otherwise, it returns 'false'.


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
     

One more feature is Copy OutputIntents from input PDF to destination PDF

We add a new public property Document.getOutputIntents() to allow access to output intents in a document.
For a time being only the usage of already existing in some document output intents is supported, user can't create OutputIntent from scratch.

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

From Aspose.PDF 23.8 support to add the shape extraction:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    //foreach to while statements conversion
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

        // Recalculate a new position since page size differs the originl PDF
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

Also supports the ability to detect Overflow when adding text:

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
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

## What's new in Aspose.PDF 23.7

From 23.7 version support the Print Dialog Presets Page Scaling:

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## What's new in Aspose.PDF 23.6

From 23.6 version support the add the ability to set the title of the HTML, Epub page.

code for HTML:

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
    epubSaveOptions.setTitle("</title>NEW PAGE & TITILE</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

From 23.6 support to provide an API for positioning vector graphics:

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
## What's new in Aspose.PDF 23.1

From 23.1 version support to create PrinterMark annotation. Added one of the annotation variant: ColorBarAnnotation.

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

## What's new in Aspose.PDF 22.12

From this release support to convert PDF to DICOM Image:


```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## What's new in Aspose.PDF 22.9

From 22.09 support adding property for modify the order of the subject rubrics (E=, CN=, O=, OU=, ) into the signature.

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
## What's new in Aspose.PDF 22.8

From Aspose.PDF 23.8 support to add method for rebuild xref table:

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


## What's new in Aspose.PDF 22.6

PDF to PDF_A_1A - implement option to remove transparency color to avoid large output file size.

From version 22.5 customer is able to control quality of converted transparency, and the output file size as a result:

```java
    opts.setTransparencyResolution(300);
```

## What's new in Aspose.PDF 22.5

During PDF/A conversion transparent content is removed and replaced with image.
We have implemented a new feature, and now the customer can control the quality of the image with the parameter TransparencyResolution:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```        

## What's new in Aspose.PDF 22.4

This release includes information for Aspose.PDF for Java:

- PDF to ODS: Recognize text in subscript and superscript;

**example**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF to XMLSpreadSheet2003: Recognize text in subscript and superscript;

- PDF to Excel: Recognize text in subscript and superscript;

## What's new in Aspose.PDF 22.3

PDF to ODS: Support for RTL is available in version 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## What's new in Aspose.PDF 22.2

This release includes the PDF to XSLX: Support for RTL (Hebrew, Arabic).

## What's new in Aspose.PDF 22.1

Aspose.PDF for Java allows loading documents Portable Document Format (PDF) version 2.0.

## What's new in Aspose.PDF 21.10

### How to detect hidden text?

Please use the following code:

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

## What's new in Aspose.PDF 21.8

### How to change text color in Digital Signature?

In the 21.8 version  setForegroundColor, it allows changing text color in Digital Signature:

```java
Please, use the following code:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    //create a rectangle for signature location
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
//set text color
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // sign the PDF file
                    pdfSign.sign(1, true, rect, pkcs);
                    //save output PDF file
                    pdfSign.save(outFile);
```

## What's new in Aspose.PDF 21.6

### Hiding image using ImagePlacementAbsorber from the document

With Aspose.PDF for Java you can hide images using ImagePlacementAbsorber from the document:

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

## What's new in Aspose.PDF 21.5

### Add API for merging images

Aspose.PDF 21.4 allows you to combine Images. Merges list of image streams as one image stream. Png/jpg/tiff outputs formats are supported, in case of using non supported format output stream encoded as Jpeg by default.
Follow the next code snippet:

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

Also you may merge you images as Tiff format:

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

## What's new in Aspose.PDF 21.02

Aspose.PDF v21.02 Sign PDF with PAdES LTV Signatures

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Sign PDF with PAdES LTV Signatures
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```