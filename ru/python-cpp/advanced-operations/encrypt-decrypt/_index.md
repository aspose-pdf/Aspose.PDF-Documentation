---
title: Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 30
url: ru/python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Шифрование и расшифровка PDF-файла с помощью Python через C++ приложение.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Шифрование PDF-файла с использованием различных типов и алгоритмов шифрования

Один из эффективных способов защиты PDF-файлов - это шифрование. В этой статье мы рассмотрим, как зашифровать PDF-документы с помощью Python с использованием библиотеки Aspose.PDF.

Шифрование PDF включает в себя кодирование содержимого PDF-документа с использованием криптографических алгоритмов для предотвращения несанкционированного доступа. Зашифрованные PDF-файлы требуют пароль для открытия и могут иметь ограничения на действия, такие как печать, копирование и редактирование.

- **Пользовательский пароль**, если установлен, это то, что вам нужно ввести, чтобы открыть PDF. Acrobat/Reader попросит пользователя ввести пользовательский пароль. Если он неверный, документ не откроется.
- **Пароль владельца**, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т. д.
 Acrobat/Reader будет запрещать эти действия в соответствии с настройками разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Следующий фрагмент кода показывает, как зашифровать файлы PDF.

1. Создание входного и выходного пути для файла
1. Загрузка PDF-документа с использованием AsposePDFPythonWrappers
1. Определение разрешений для зашифрованного документа
1. Определение алгоритма шифрования для использования
1. Шифрование документа с указанными паролями пользователя и владельца, разрешениями и алгоритмом шифрования с использованием метода 'document.encrypt'
1. Сохранение зашифрованного документа в указанный выходной файл с помощью метода 'document.save'.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Установите путь к каталогу для примеров файлов
    dataDir = os.path.join(os.getcwd(), "samples")

    # Установите путь к входному файлу
    input_file = os.path.join(dataDir, "sample.pdf")

    # Установите путь к выходному файлу
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # Загрузка PDF-документа с использованием AsposePDFPythonWrappers
    document = apw.Document(inputFile)

    # Определение разрешений для зашифрованного документа
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # Определение алгоритма шифрования для использования
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # Шифрование документа с указанными паролями пользователя и владельца, разрешениями и алгоритмом шифрования
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # Сохранение зашифрованного документа в указанный выходной файл
    document.save(output_file)
```

## Расшифровать PDF файл с использованием пароля владельца

1. Создание пути для входного и выходного файла
1. Создайте новый экземпляр класса Document из модуля AsposePDFPythonWrappers
1. Расшифруйте документ, используя метод [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/)
1. Сохраните расшифрованный документ в путь выходного файла, используя метод save() с функцией [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/).

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Установите путь к директории для примеров файлов
    dataDir = os.path.join(os.getcwd(), "samples")

    # Установите путь к входному файлу
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # Установите путь к выходному файлу
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # Создайте новый экземпляр класса Document из модуля AsposePDFPythonWrappers
    document = apw.Document(input_file, "owner")

    # Расшифруйте документ, используя метод decrypt()
    document.decrypt()

    # Сохраните расшифрованный документ в путь выходного файла, используя метод save()
    document.save(output_file)
```