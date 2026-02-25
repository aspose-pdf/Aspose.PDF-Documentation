---
title: 在 Python 中添加数字签名或对 PDF 进行数字签名
linktitle: 数字签名 PDF
type: docs
weight: 10
url: /zh/python-net/digitally-sign-pdf-file/
description: 使用 Python 对 PDF 文档进行数字签名、验证或校验已数字签名的 PDF。
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 对 PDF 文件进行数字签名
Abstract: 本指南说明了如何使用 Aspose.PDF for Python via .NET 对 PDF 文档进行数字签名。它详细介绍了应用标准和高级数字签名的过程，使用证书（PFX 和 PKCS#12），以及自定义签名外观和行为。文档包含代码示例，演示如何对现有 PDF 进行签名、添加时间戳以及验证签名的有效性。这使开发者能够在其 Python 应用程序中确保文档的真实性、完整性并符合数字签名标准。
---

## 使用数字签名签署 PDF

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

**PKCS#7 分离签名** 为文档添加数字签名，而不将内容嵌入签名块中。

下面的示例使用 PKCS#7 分离数字签名对 PDF 文档进行签名，将签名应用于指定矩形区域的第一页。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

此 Python 代码片段使用 'file_sign.verify_signature()' 方法验证 PDF 文件中的数字签名。

1. 创建一个 PdfFileSignature 实例，以便与 PDF 中的签名进行交互。
1. 获取签名名称列表 `get_signature_names(True)`。
1. 检查列表中的第一个签名 `verify_signature` 是否符合指定证书。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## 为数字签名添加时间戳

### 如何为 PDF 添加时间戳进行数字签名

Aspose.PDF for Python 支持使用时间戳服务器或 Web 服务对 PDF 进行数字签名。

为了实现此需求，已在 Aspose.PDF 命名空间中添加了 [时间戳设置](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) 类。请查看下面的代码片段，它获取时间戳并将其添加到 PDF 文档中：

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## 使用 ECDSA 签署 PDF 文档

使用 ECDSA（椭圆曲线数字签名算法）签署 PDF 文档涉及利用椭圆曲线密码学生成数字签名。

上面的代码片段展示了如何使用 Aspose.PDF for Python 对 PDF 文档应用 PKCS#7 分离数字签名。通过加载文档、配置签名外观和安全设置并保存结果，该示例演示了一个完整且可靠的 PDF 文件数字签名工作流。

此方法通过在首页嵌入安全且可验证的签名，确保文档的真实性和完整性。使用 SHA-256 作为摘要算法符合现代密码学标准，同时能够控制签名位置，为可见的批准标记提供了灵活性。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
