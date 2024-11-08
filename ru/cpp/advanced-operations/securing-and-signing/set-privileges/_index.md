---
title: Установить Привилегии, Шифровать и Расшифровать PDF Файл с использованием C++
linktitle: Шифровать и Расшифровать PDF Файл
type: docs
weight: 20
url: /ru/cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: шифровать pdf,защитить паролем pdf,расшифровать pdf,c++
description: Шифровать PDF Файл с использованием C++ с различными типами и алгоритмами шифрования. Также, расшифровать PDF Файлы с использованием пароля владельца.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Установить Привилегии на Существующий PDF Файл

Для установки привилегий на существующий PDF файл Aspose.PDF for C++ используйте класс [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) и укажите права, которые вы хотите применить к документу. После того как привилегии были определены, передайте этот объект в качестве аргумента методу [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Следующий фрагмент кода показывает, как установить привилегии PDF файла.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Загрузка исходного PDF файла
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Создание объекта привилегий документа

    // Применение ограничений на все привилегии
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Разрешить только чтение с экрана
    documentPrivilege->set_AllowScreenReaders(true);

    // Шифрование файла с использованием пароля пользователя и владельца.
    // Необходимо установить пароль, чтобы, когда пользователь откроет файл с паролем пользователя,

    // Была включена только опция чтения с экрана
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // Сохранение обновленного документа
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Шифрование PDF файла с использованием различных типов и алгоритмов шифрования

Для шифрования PDF файла используйте метод [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) для шифрования PDF файла.


Следующий фрагмент кода показывает, как зашифровать PDF файлы.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // Строка для пути.
    String _dataDir("C:\\Samples\\");

    // Загрузите исходный PDF файл
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Создайте объект привилегий документа
    // Примените ограничения ко всем привилегиям
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Разрешить только чтение с экрана
    documentPrivilege->set_AllowScreenReaders(true);
    // Зашифруйте файл с паролем пользователя и владельца.
    // Необходимо установить пароль, чтобы, когда пользователь просматривает файл с паролем пользователя,
    // была доступна только опция чтения с экрана
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // Сохраните обновленный документ
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Расшифровка PDF файла с использованием пароля владельца

Для того чтобы расшифровать PDF файл, вам сначала нужно создать объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) и открыть PDF с использованием пароля владельца. После этого вам нужно вызвать метод [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a).

```cpp
void SecuringAndSigning::DecryptPDFFile() {

// Строка для имени пути.

String _dataDir("C:\\Samples\\");

// Открыть документ

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// Расшифровать PDF

document->Decrypt();

// Сохранить обновленный PDF

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## Изменение пароля PDF-файла

Поскольку ваши PDF могут содержать важную и конфиденциальную информацию, они должны оставаться в безопасности. Соответственно, вам может потребоваться изменить пароль вашего PDF-документа.

Если вы хотите изменить пароль PDF-файла, вам сначала нужно открыть PDF-файл, используя пароль владельца с объектом [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). После этого вам нужно вызвать метод [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d).

Следующий фрагмент кода показывает, как изменить пароль PDF-файла.
```cpp
void SecuringAndSigning::ChangePassword_PDF_File() {

// String for path name.

String _dataDir("C:\\Samples\\");


// Open document

auto document = MakeObject<Document>(_dataDir + u"ChangePassword.pdf", u"owner");

// Change password

document->ChangePasswords(u"owner", u"newuser", u"newowner");

// Save updated PDF

document->Save(_dataDir + u"ChangePassword_out.pdf");
}
```

## Как определить, защищен ли исходный PDF паролем

Документ PDF, зашифрованный паролем пользователя, не может быть открыт без пароля. Мы должны сначала определить, защищен ли документ паролем, прежде чем пытаться его открыть. Иногда существуют документы, которые не требуют информации о пароле при открытии, но требуют информации для редактирования содержимого файла. Поэтому, чтобы выполнить вышеуказанные требования, класс [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) из Aspose.PDF.Facades предоставляет свойства, которые могут помочь в определении необходимой информации.

### Получение информации о безопасности документа PDF

PdfFileInfo содержит три свойства для получения информации о безопасности документа PDF.

1. свойство PasswordType возвращает значение перечисления PasswordType:
    - PasswordType.None - документ не защищен паролем
    - PasswordType.User - документ был открыт с использованием пользовательского (или открытого) пароля
    - PasswordType.Owner - документ был открыт с использованием пароля владельца (или разрешений, редактирование)

    - PasswordType.Inaccessible - документ защищен паролем, но для его открытия необходим пароль, при этом был указан неверный пароль (или пароль отсутствует).2. логическое свойство HasOpenPassword - используется для определения, требует ли входной файл пароль при его открытии.  
3. логическое свойство HasEditPassword - используется для определения, требует ли входной файл пароль для редактирования его содержимого.

### Определение правильного пароля из массива

Иногда требуется определить правильный пароль из массива паролей и открыть документ с правильным паролем. Следующий фрагмент кода демонстрирует шаги по перебору массива паролей и попытке открыть документ с правильным паролем.

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {

// Строка для имени пути.

String _dataDir("C:\\Samples\\");

// Загрузить исходный PDF файл

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");

// Определить, зашифрован ли исходный PDF

Console::WriteLine(u"Файл защищен паролем {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };

for (int passwordcount = 0; passwordcount < count; passwordcount++)

{

try

{

auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);

auto pages = document->get_Pages()->get_Count();

if (pages > 0)

Console::WriteLine(u"Количество страниц в документе = {0}", pages);

}

catch (Aspose::Pdf::InvalidPasswordException ex)

{

Console::WriteLine(u"Пароль = {0} неверный", passwords[passwordcount]);

}

}

Console::WriteLine(u"Тест завершен");
}
```