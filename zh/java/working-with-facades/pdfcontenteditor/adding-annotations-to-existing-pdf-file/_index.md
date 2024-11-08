---

title: 向现有 PDF 文件添加注释

type: docs

weight: 80

url: /zh/java/adding-annotations-to-existing-pdf-file/

description: 本节解释如何使用 Aspose.PDF Facades 向现有 PDF 文件添加注释。

lastmod: "2021-06-30"

sitemap:

​    changefreq: "monthly"

​    priority: 0.7

---

## 在现有 PDF 文件中添加自由文本注释 (facades)

自由文本注释直接在页面上显示文本。[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 允许您在现有的 PDF 文件中添加不同类型的注释。您可以使用相应的方法添加特定的注释。例如，在以下代码片段中，我们使用了 [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) 方法来添加 FreeText 类型的注释。

任何类型的注释都可以以相同的方式添加到 PDF 文件中。
 首先，您需要创建一个类型为 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 的对象，并使用 bindPdf 方法绑定输入的 PDF 文件。其次，您需要创建一个 Rectangle 对象来指定注释的区域。之后，您可以调用 [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) 方法添加自由文本注释，注释所在的页码，然后使用 save 方法保存更新后的 PDF 文件。

以下代码片段展示了如何在 PDF 文件中添加自由文本注释。

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Free Text Demo", 1); // 最后一个参数是页码
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## 在现有 PDF 文件中添加文本注释 (facades)

在这个例子中，你需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类型的对象，并使用 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-) 方法绑定输入的 PDF 文件。其次，你需要创建一个矩形对象以指定注释的区域。之后，你可以调用 [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) 方法来添加自由文本注释，创建注释的标题以及注释所在的页码。

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## 在现有 PDF 文件中添加线注释（外观）

我们还指定矩形、线的起始和结束坐标、页码、注释框架的厚度、样式和颜色，线条虚线类型，线条起始和结束类型。

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // 创建线注释
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```