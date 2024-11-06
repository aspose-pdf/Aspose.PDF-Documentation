---
title: Установка Привилегий на PDF
type: docs
weight: 50
url: ru/net/set-privileges/
description: Эта тема объясняет, как установить привилегии на существующий PDF файл с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Установка Привилегий на Существующий PDF Файл

Чтобы установить привилегии для PDF файла, создайте объект [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) и вызовите метод SetPrivilege. Вы можете указать привилегии, используя объект DocumentPrivilege, а затем передать этот объект в метод SetPrivilege. В следующем коде показано, как установить привилегии PDF файла.

```csharp
public static void SetPrivilege1()
 {
    // Создайте объект DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Создайте объект PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

See the following method with specifying a password:

```csharp
 public static void SetPrivilege2()
 {
    // Создайте объект DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Создайте объект PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## Удаление функции расширенных прав из PDF

PDF документы поддерживают функцию расширенных прав, чтобы позволить конечному пользователю заполнять данные в поля формы с помощью Adobe Acrobat Reader и затем сохранять копию заполненной формы. Однако это гарантирует, что PDF файл не был изменен, и если в структуру PDF внесены какие-либо изменения, функция расширенных прав теряется. При просмотре такого документа отображается сообщение об ошибке, указывающее, что расширенные права удалены, так как документ был изменен. Недавно мы получили запрос на удаление расширенных прав из PDF документа.

Для удаления расширенных прав из PDF файла в класс PdfFileSignature добавлен новый метод под названием RemoveUsageRights(). Другой метод под названием ContainsUsageRights() добавлен для определения, содержит ли исходный PDF расширенные права.

{{% alert color="primary" %}}
Начиная с Aspose.PDF for .NET 9.5.0, названия следующих методов были обновлены. Обратите внимание, что предыдущие методы все еще находятся в API, но они были помечены как устаревшие и будут удалены. Поэтому рекомендуется использовать обновленные методы.

- Метод IsContainSignature(.) был переименован в ContainsSignature(..).

- Метод IsCoversWholeDocument(..) был переименован в CoversWholeDocument(..).{{% /alert %}}

Следующий код показывает, как удалить права использования из документа:

```csharp
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```