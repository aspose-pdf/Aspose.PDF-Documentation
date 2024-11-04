---
title: Быстрые советы
type: docs
weight: 50
url: /java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Эта страница содержит некоторые быстрые советы, связанные с Aspose.PDF для Java API

{{% /alert %}}

## Добавление JavaScript в PDF

Следующий фрагмент кода может быть использован для установки/добавления JavaScript в PDF файл.

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //Добавление JavaScript на уровне документа
    //Создание JavascriptAction с желаемым JavaScript выражением
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //Назначение объекта JavascriptAction желаемому действию документа
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //Добавление JavaScript на уровне страницы
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**Еще несколько примеров**

```java

// после печати
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('Файл был напечатан')"));

// после сохранения
document.getActions().setAfterSaving(new JavascriptAction("app.alert('Файл был сохранен')"));

```

## Освобождение используемой памяти

Если вы завершили работу с Aspose.PDF для Java и хотите очистить память от различных статических экземпляров, чтобы освободить максимальное количество памяти для других процессов, вам следует выполнить следующую строку кода:

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## Загрузка PDF из ByteArrayInputStream

Следующий фрагмент кода показывает шаги загрузки PDF-файла в ByteArray, а затем создания объекта Document с ByteArrayInputStream.

```java

 // исходный PDF файл

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //несомненно, здесь 0

        //Записывает len байтов из указанного массива байтов, начиная с смещения off, в этот выходной поток массива байтов.

        System.out.println("прочитано " + readNum + " байтов,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// создание объекта Document с помощью ByteArrayInputStream, передавая массив байтов в качестве аргумента

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// получить количество страниц в PDF файле

 System.out.println(doc.getPages().size());

```


## Сохранение PDF в ByteArrayOutputStream

Следующий фрагмент кода показывает шаги для сохранения итогового PDF файла в ByteArrayOutputStream.

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```