---
title: Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 30
url: /python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: 使用Python通过C++应用程序加密和解密PDF文件。
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用不同的加密类型和算法加密PDF文件

保护PDF文件的一个有效方法是通过加密。在本文中，我们将探讨如何使用Python结合Aspose.PDF库来加密PDF文档。

PDF加密涉及使用加密算法对PDF文档的内容进行加扰，以防止未经授权的访问。加密的PDF文件需要密码才能打开，并且可能对打印、复制和编辑等操作有限制。

- **用户密码**，如果设置，这是打开PDF时需要提供的密码。Acrobat/Reader会提示用户输入用户密码。如果不正确，文档将不会打开。
- **所有者密码**，如果设置，它控制权限，如打印、编辑、提取、评论等。
 Acrobat/Reader 将根据权限设置禁止这些操作。如果您想设置/更改权限，Acrobat 将需要此密码。

以下代码片段向您展示了如何加密 PDF 文件。

1. 创建输入和输出文件路径
2. 使用 AsposePDFPythonWrappers 加载 PDF 文档
3. 定义加密文档的权限
4. 定义要使用的加密算法
5. 使用 'document.encrypt' 方法，用指定的用户和所有者密码、权限和加密算法加密文档
6. 使用 'document.save' 方法将加密的文档保存到指定的输出文件。

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # 设置示例文件的目录路径
    dataDir = os.path.join(os.getcwd(), "samples")

    # 设置输入文件路径
    input_file = os.path.join(dataDir, "sample.pdf")

    # 设置输出文件路径
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # 使用 AsposePDFPythonWrappers 加载 PDF 文档
    document = apw.Document(inputFile)

    # 定义加密文档的权限
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # 定义要使用的加密算法
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # 使用指定的用户和所有者密码、权限和加密算法加密文档
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # 将加密的文档保存到指定的输出文件
    document.save(output_file)
```

## 使用所有者密码解密 PDF 文件

1. 创建输入和输出文件路径
1. 从 AsposePDFPythonWrappers 模块创建 Document 类的新实例
1. 使用 [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/) 方法解密文档
1. 使用带有 [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/) 函数的 save() 方法将解密后的文档保存到输出文件路径

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # 设置示例文件的目录路径
    dataDir = os.path.join(os.getcwd(), "samples")

    # 设置输入文件路径
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # 设置输出文件路径
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # 从 AsposePDFPythonWrappers 模块创建 Document 类的新实例
    document = apw.Document(input_file, "owner")

    # 使用 decrypt() 方法解密文档
    document.decrypt()

    # 使用 save() 方法将解密后的文档保存到输出文件路径
    document.save(output_file)
```