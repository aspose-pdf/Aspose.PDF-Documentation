---
title: 合并PDF文档
type: docs
weight: 10
url: /java/concatenate-pdf-documents/
description: 本节解释如何使用PdfFileEditor类通过com.aspose.pdf.facades合并PDF文档。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用文件路径合并PDF文件 (Facades)

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 类的concatenate方法可以用来合并两个PDF文件。concatenate方法允许你传递三个参数：第一个输入PDF，第二个输入PDF，以及输出PDF。最终的输出PDF包含两个输入PDF文件。

以下代码片段展示了如何使用文件路径合并PDF文件。

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // 创建PdfFileEditor对象
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 合并文件
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


在某些情况下，当有很多大纲时，用户可以通过将 **CopyOutlines** 设置为 false 来禁用它们，并提高连接的性能。

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // 创建 PdfFileEditor 对象
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 合并文件
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## 使用 MemoryStreams 连接多个 PDF 文件

[Concatenate]https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 类将源 PDF 文件和目标 PDF 文件作为参数。
 这些参数可以是磁盘上的PDF文件路径，也可以是MemoryStreams。现在，在这个示例中，我们将首先创建两个文件流来从磁盘读取PDF文件。然后我们将这些文件转换为字节数组。这些PDF文件的字节数组将被转换为MemoryStreams。一旦我们从PDF文件中获得MemoryStreams，我们就可以将它们传递给连接方法并合并为一个输出文件。

以下代码片段展示了如何使用MemoryStreams连接多个PDF文件：

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // 创建两个文件流以读取PDF文件
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // 创建字节数组以保存PDF文件的内容
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.le)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // 将PDF文件内容读取到字节数组中
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // 现在，首先将字节数组转换为MemoryStreams，然后连接这些流
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // 创建PdfFileEditor类的实例以连接流
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // 连接两个输入MemoryStreams并保存到输出MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // 将MemoryStream转换回字节数组
                        byte[] data = pdfStream.ToArray();
                        // 创建一个FileStream以保存输出PDF文件
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // 将字节数组内容写入输出文件流
                        output.Write(data, 0, data.Length);
                        // 关闭输出文件
                        output.Close();
                    }
                }
            }
            // 关闭输入文件
            fs1.Close();
            fs2.Close();
        }
```

## 使用文件路径连接 PDF 文件数组（Facades）

如果您想连接多个 PDF 文件，可以使用连接方法的重载，它允许您传递 PDF 文件路径的数组。最终输出保存为由数组中所有文件创建的合并文件。

以下代码段向您展示如何使用文件路径连接 PDF 文件数组。

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // 创建 PdfFileEditor 对象
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 文件数组
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // 连接文件
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## 使用流连接 PDF 文件数组（Facades）

连接 PDF 文件数组不仅限于仅驻留在磁盘上的文件。
 你也可以从流中连接一个PDF文件数组。如果你想连接多个PDF文件，可以使用Concatenate方法的相应重载。首先，你需要创建一个输入流数组和一个用于输出PDF的流，然后调用Concatenate方法。输出将保存在输出流中。

以下代码片段展示了如何使用流连接PDF文件数组。

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // 创建PdfFileEditor对象
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // 流数组
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // 输出流
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // 连接文件
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## 合并 PDF 表单并保持字段名称唯一

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 类在 [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) 命名空间中提供了合并 PDF 文件的功能。
 现在，如果要连接的 PDF 文件包含具有相似字段名称的表单字段，Aspose.PDF 提供了使生成的 PDF 文件中的字段唯一的功能，并且您可以指定后缀以使字段名称唯一。PdfFileEditor 的 [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) 方法为 true 时，将在连接 PDF 表单时使字段名称唯一。此外，PdfFileEditor 的 [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) 方法可用于指定后缀的用户定义格式，该后缀在表单连接时被添加到字段名称以使其唯一。此字符串必须包含 %NUM% 子字符串，该子字符串将在生成的文件中用数字替换。

请参阅以下简单代码片段以实现此功能。

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // 设置输入和输出文件路径

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // 实例化 PdfFileEditor 对象
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // 保持所有字段的唯一字段 ID
                KeepFieldsUnique = true,
                // 表单连接时添加到字段名称以使其唯一的后缀格式。
                UniqueSuffix = "_%NUM%"
            };

            // 将文件连接成一个生成的 Pdf 文件
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## 合并插入空白页

一旦PDF文件合并完成，我们可以在文档的开头插入一个空白页，在其上可以创建目录。为了实现这一需求，我们可以将合并后的文件加载到Document对象中，并需要调用Page.Insert(…)方法来插入一个空白页。

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // 创建 PdfFileEditor 对象
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // 合并文件
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```