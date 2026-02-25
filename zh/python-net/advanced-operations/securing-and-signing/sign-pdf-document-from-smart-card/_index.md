---
title: 如何在 PDF 中添加智能卡签名
linktitle: 使用智能卡进行 PDF 签名
type: docs
weight: 30
url: /zh/python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for Python via .NET 允许您使用签名字段通过智能卡对 PDF 文档进行签名。
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从智能卡签署 PDF 文档
Abstract: 本指南解释了如何使用 Aspose.PDF for Python via .NET 通过智能卡对 PDF 文档进行数字签名。它演示了如何通过 Windows 证书存储访问存储在硬件设备（如 USB 令牌或智能卡）上的证书，并将其用于签署 PDF 文件。文档包含代码示例，展示如何定位适当的证书、配置签名属性以及将数字签名嵌入 PDF。此方法实现了符合数字签名标准的安全硬件支持签名，适用于高信任的企业和法律工作流。
---

Aspose.PDF 提供了强大的功能，可集成可视化和加密签名组件，确保数字签名 PDF 文档的真实性和专业呈现。

## 使用签名字段的智能卡签名

此示例演示如何使用 Aspose.PDF for Python 通过外部证书对 PDF 文档进行数字签名，并应用自定义签名外观图像：

1. 打开 PDF 文档。
1. 创建 PdfFileSignature 对象并将其绑定到文档。
1. 使用自定义方法 `get_local_certificate()` 检索本地数字证书。
1. 基于所选证书设置 ExternalSignature。
1. 应用自定义签名外观图像（例如公司徽标或手写签名）。
1. 使用指定的元数据（原因、联系人、位置）对文档的首页进行数字签名。
1. 将已签名的文档保存为新的输出文件。

此方法非常适用于需要使用外部证书（如硬件令牌、证书存储或受信任提供商）以编程方式应用签名，并呈现个性化视觉布局的情况。

以下是从智能卡签署 PDF 文档的代码片段：

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## 验证数字签名

此代码片段演示了如何使用 Aspose.PDF for Python 验证 PDF 文档中的数字签名：

1. 打开 PDF 文件。
1. 创建 'PdfFileSignature 对象' 并将其绑定到文档。
1. 使用 'get_signature_names()' 检索所有签名字段名称的列表。
1. 遍历每个签名并使用 'verify_signature()' 验证其有效性。
1. 如果任何签名验证失败，则抛出异常。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## 使用外部证书签名

此代码片段演示了如何使用 Aspose.PDF for Python 及外部证书在 PDF 文档中添加并签署数字签名字段：

1. 将 PDF 文件以二进制流方式打开。
1. 创建 SignatureField 并将其放置在文档首页的指定位置。
1. 使用自定义方法 `get_local_certificate()` 检索本地数字证书。
1. 使用诸如授权方、原因和联系信息等元数据设置 ExternalSignature。
1. 为签名字段分配唯一字段名称（partial_name = "sig1"）。
1. 将签名字段添加到 PDF 的表单字段中。
1. 使用外部证书对字段进行签名。
1. 将已签名的文档保存为输出文件。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```


