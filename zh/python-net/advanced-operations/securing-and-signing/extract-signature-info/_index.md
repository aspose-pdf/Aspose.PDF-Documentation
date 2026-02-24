---
title: 提取签名详细信息
linktitle: 提取签名详细信息
type: docs
weight: 20
url: /zh/python-net/extract-image-and-signature-information/
description: 如何使用 Aspose.PDF for Python 从 PDF 文档中的数字签名提取图像。
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中获取签名详细信息
Abstract: 本文演示了如何使用 Aspose.PDF for Python 从 PDF 文档中提取图像和数字签名信息。它提供了逐步说明和代码示例，帮助识别、访问和保存嵌入的图像，以及检索数字签名的元数据和验证状态。
---

## 从签名字段提取图像

Aspose.PDF for Python via .NET 支持使用 [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) 类对 PDF 文件进行数字签名。

此代码片段演示了如何使用 Aspose.PDF for Python 从 PDF 文档中提取数字签名图像。

步骤：

1. 打开 PDF 文档。
1. 遍历表单字段以定位任何 SignatureField 对象。
1. 提取与每个签名关联的图像（如果有）。
1. 将提取的签名图像保存为 JPEG 文件。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue

            image_stream = signature_field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            # Save the image
            image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## 提取签名信息

Aspose.PDF for Python via .NET 支持使用 SignatureField 类对 PDF 文件进行数字签名。当前，我们也可以确定证书的有效性，但无法提取完整的证书。可以提取的信息包括公钥、指纹、颁发者等。

为了提取签名信息，我们在 [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) 类中引入了 [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) 方法。请查看下面的代码片段，演示从 SignatureField 对象提取证书的步骤：

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue
            # Extract certificate
            certificate_stream = signature_field.extract_certificate()
            if certificate_stream is None:
                continue
            # Save certificate
            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                with open(path_outfile, "wb") as file_stream:
                    certificate_stream.read(bytes_data, 0, len(bytes_data))
                    file_stream.write(bytes_data)
```

您可以获取文档签名算法的信息。

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            signatures_info_list = signature.get_signatures_info()
            for sig_info in signatures_info_list:
                print(sig_info.DIGEST_HASH_ALGORITHM)
                print(sig_info.ALGORITHM_TYPE)
                print(sig_info.CRYPTOGRAPHIC_STANDARD)
                    print(sig_info.signature_name)
```

## 检查签名是否被破坏

此代码片段演示了如何使用 Aspose.PDF for Python 检测 PDF 文档中受损的数字签名。

步骤包括：

1. 打开 PDF 文档。
1. 创建一个 'SignaturesCompromiseDetector' 实例来分析文档。
1. 检查是否存在任何受损（无效或被更改）的数字签名。
1. 打印发现的受损签名的名称。
1. 报告签名覆盖率——指示文档中有多少已被有效签名保护。

此功能在必须验证文档真实性和完整性的使用场景中至关重要，例如法律、金融和合规驱动的环境。它使开发者能够自动检测已签署 PDF 的篡改或损坏。

Aspose.PDF 提供了一套全面的数字签名验证工具，使构建安全、具备签名感知的应用程序更为容易，从而维护文档的可信度。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create the compromise detector instance
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        # Check for compromise
        if detector.check(result):
            print("No signature compromise detected")
            return

        # Get information about compromised signatures
        if result[0].has_compromised_signatures:
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```

