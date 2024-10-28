---
title: Migration from legacy Aspose.Pdf.Kit for Java
type: docs
weight: 10
url: /java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Текущий компонент Aspose.PDF.Kit for Java предоставлял функции для управления существующими PDF-файлами. Однако вскоре этот компонент будет прекращен как отдельный продукт, потому что мы перенесли все его классы и перечисления в пакет **com.aspose.pdf.facades** нового автоматического релиза Aspose.PDF for Java (4.x.x). Теперь этот единый автоматический релиз предоставляет возможности как для создания, так и для управления существующими PDF-файлами.

{{% /alert %}}

## Поддержка устаревшего кода

Во время всей миграционной активности мы, безусловно, учитывали воздействие этой активности на существующих клиентов и старались максимально минимизировать это воздействие.
 Кроме того, мы также сосредоточились на том, чтобы сделать новый автопортированный релиз обратно совместимым, чтобы кодовая база существующих клиентов требовала минимальных изменений. Хотя новый автопортированный релиз предоставляет объектную модель документа (DOM) в пакете com.aspose.pdf для создания и управления существующими PDF-файлами, если вы хотите продолжать использовать ваш устаревший код, разработанный с помощью Aspose.PDF.Kit for Java, вам нужно только импортировать пакет **com.aspose.pdf.facades** и ваш код должен работать (*за исключением обновления явных ссылок на классы*).

Следующий фрагмент кода показывает, как запустить ваш существующий код Aspose.PDF.Kit for Java с новым автопортированным Aspose.PDF for Java.

```java

 import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // загрузить существующий PDF файл

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("TITLE: " + fileInfo.getTitle());

            System.out.println("AUTHOR:" + fileInfo.getAuthor());

            System.out.println("CREATIONDATE:" + fileInfo.getCreationDate());

            System.out.println("CREATOR:" + fileInfo.getCreator());

            System.out.println("KeyWORDS:" + fileInfo.getKeywords());

            System.out.println("MODDATE:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## Использование класса ReplaceTextStrategy

Для миграции кода для класса ReplaceTextStrategy метод **setScope(..)** был обновлён до **setReplaceScope(..)**. Пожалуйста, обратите внимание на следующий фрагмент кода.

```java

// создать экземпляр объекта PdfContentEditor

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// привязать исходный PDF файл

editor.bindPdf("input.pdf");

// создать стратегию замены текста

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// установить выравнивание для замены текста

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// область для замены текста

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// установить стратегию замены

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// сохранить обновлённый файл

editor.save("TxtReplaceTest.pdf");
```