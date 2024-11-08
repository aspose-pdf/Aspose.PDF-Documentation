---
title: Установить Привилегии, Зашифровать и Расшифровать PDF Файл
linktitle: Зашифровать и Расшифровать PDF Файл
type: docs
weight: 20
url: /ru/java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: зашифровать pdf, защита паролем pdf, расшифровать pdf, java
description: Зашифровать PDF файл с использованием различных типов и алгоритмов шифрования на языке Java. Также, расшифровать PDF файлы с использованием пароля владельца.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Установить Привилегии на Существующий PDF Файл

Чтобы установить привилегии на PDF файл, создайте объект класса DocumentPrivilege и укажите права, которые вы хотите применить к документу.
 Как только привилегии были определены, передайте этот объект в качестве аргумента методу [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Следующий фрагмент кода показывает, как установить привилегии PDF файла.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // Загрузить исходный PDF файл
   Document document = new Document(_dataDir + "input.pdf");

   // Создать объект Document Privileges
   // Применить ограничения на все привилегии
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Разрешить только экранное чтение
   documentPrivilege.setAllowScreenReaders(true);
   // Зашифровать файл с паролем пользователя и владельца.
   // Необходимо установить пароль, чтобы, когда пользователь просматривает файл с паролем пользователя,
   // Была включена только опция экранного чтения
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Сохранить обновленный документ
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Шифрование PDF-файла с использованием различных типов и алгоритмов шифрования

Вы можете использовать метод [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) для шифрования PDF-файла. Вы можете передать пользовательский пароль, пароль владельца и разрешения в метод [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-). Кроме того, вы можете передать любое значение из перечисления [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm). Это перечисление предоставляет различные комбинации алгоритмов шифрования и размеров ключей. Вы можете передать значение по вашему выбору. Наконец, сохраните зашифрованный PDF-файл, используя метод [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

>Пожалуйста, указывайте разные пароли для пользователя и владельца при шифровании PDF-файла.

Следующий фрагмент кода показывает, как зашифровать PDF файлы.

```java
public static void EncryptPDFFile() {
   // Загрузите исходный PDF файл
   Document document = new Document(_dataDir + "input.pdf");

   // Создайте объект привилегий документа
   // Примените ограничения ко всем привилегиям
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Разрешить только чтение с экрана
   documentPrivilege.setAllowScreenReaders(true);
   // Зашифровать файл с помощью пароля пользователя и владельца.
   // Необходимо установить пароль, чтобы, когда пользователь откроет файл с паролем пользователя,
   // была доступна только опция чтения с экрана
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Сохранить обновленный документ
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Расшифровка PDF файла с использованием пароля владельца

Чтобы расшифровать PDF файл, вам необходимо сначала создать объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и открыть PDF, используя пароль владельца.
 После этого вам нужно вызвать метод [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Наконец, сохраните обновленный PDF файл, используя метод Save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Следующий фрагмент кода показывает, как расшифровать PDF файл.

```java
public static void DecryptPDFFile() {
   // Открыть документ
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // Расшифровать PDF
   document.decrypt();

   // Сохранить обновленный PDF
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## Изменение пароля PDF файла

Если вы хотите изменить пароль PDF файла, сначала нужно открыть PDF файл, используя пароль владельца с объектом [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). После этого вам нужно вызвать метод [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Вам необходимо передать текущий пароль владельца вместе с новым паролем пользователя и новым паролем владельца этому методу. Наконец, сохраните обновленный PDF-файл, используя метод Save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает, как изменить пароль PDF-файла.

```java
public static void ChangePassword_PDF_File() {
   // Открыть документ
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // Изменить пароль
   document.changePasswords("owner", "newuser", "newowner");
   // Сохранить обновленный PDF
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## Как определить, защищен ли исходный PDF паролем

Aspose.PDF для Java предоставляет отличные возможности для работы с PDF-документами. When using [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class of com.aspose.pdf package to open a PDF document which is password protected, we need to provide the password information as an argument to Document constructor and in case this information is not provided, an error message is generated. In fact when trying to open a PDF file with Document object, the constructor is trying to read the contents of PDF file and in case correct password is not provided, an error message is generated (it happens to prevent unauthorised access of document)

При использовании класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) из пакета com.aspose.pdf для открытия PDF-документа, защищенного паролем, нам необходимо предоставить информацию о пароле в качестве аргумента для конструктора Document. В случае, если эта информация не предоставлена, генерируется сообщение об ошибке. На самом деле, при попытке открыть PDF-файл с помощью объекта Document, конструктор пытается прочитать содержимое PDF-файла, и в случае, если правильный пароль не предоставлен, генерируется сообщение об ошибке (это происходит для предотвращения несанкционированного доступа к документу).

When dealing with encrypted PDF files, you may come across the scenario where you would be interested to detect if a PDF has an open password and/or an edit password.

При работе с зашифрованными PDF-файлами вы можете столкнуться с ситуацией, когда вам будет интересно определить, есть ли у PDF файла пароль для открытия и/или пароль для редактирования. Иногда существуют документы, которые не требуют ввода пароля при их открытии, но требуют информацию для редактирования содержимого файла. Таким образом, для выполнения вышеуказанных требований, класс PdfFileInfo, представленный в пакете com.aspose.pdf.facades, предоставляет методы, которые могут помочь в определении требуемой информации.

### Получение информации о безопасности PDF документа

PdfFileInfo содержит три метода для получения информации о безопасности PDF документа.

1. Метод getPasswordType() возвращает значение перечисления PasswordType:
    1. PasswordType.None - документ не защищен паролем
    1. PasswordType.User - документ был открыт с пользовательским паролем (или паролем открытия документа)
    1. PasswordType.Owner - документ был открыт с паролем владельца (или паролем разрешений, редактирования)
    1. PasswordType.Inaccessible - документ защищен паролем, но для его открытия требуется пароль, в то время как был введен неверный пароль (или пароль не был введен).
1. Метод hasOpenPassword() используется для определения, требует ли входной файл пароль при его открытии.
1. Метод hasEditPassword() используется для определения, требует ли входной файл пароль для редактирования его содержимого.

### Определение правильного пароля из массива

Иногда возникает необходимость определить правильный пароль из массива паролей и открыть документ с правильным паролем. Следующий фрагмент кода демонстрирует шаги по перебору массива паролей и попытке открыть документ с правильным паролем.

```java
public static void DetermineCorrectPasswordFromArray() {
     // Загрузить исходный PDF файл
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // Определить, зашифрован ли исходный PDF
   System.out.println("Файл защищен паролем " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("Количество страниц в документе = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("Пароль = " + passwords[passwordcount] + "  не является правильным");
    }
   }
```