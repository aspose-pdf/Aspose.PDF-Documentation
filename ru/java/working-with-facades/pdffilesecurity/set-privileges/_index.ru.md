---
title: Установка Привилегий на Существующий PDF Файл
type: docs
weight: 50
url: /java/set-privileges/
description: Эта тема объясняет, как установить привилегии на существующий PDF файл, используя класс PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Установка Привилегий на Существующий PDF Файл (фасады)

Чтобы установить привилегии PDF файла, создайте объект класса [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) и привяжите входной PDF, используя метод bindPdf. Затем вам нужно вызвать метод setPrivilege, чтобы установить привилегии. Вы можете указать привилегии, используя объект [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege), а затем передать этот объект в метод setPrivilege и сохранить выходной PDF, используя метод save.

Следующий фрагмент кода показывает, как установить привилегии PDF файла.

```java
public static void SetPrivilege1() {
        // Создать объект DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Создать объект PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


Смотрите следующий метод с указанием пароля:

```java
 public static void SetPrivilege2() {
        // Создать объект DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Создать объект PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```