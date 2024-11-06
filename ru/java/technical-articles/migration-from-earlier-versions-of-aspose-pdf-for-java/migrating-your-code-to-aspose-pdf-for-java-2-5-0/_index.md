---
title: Перенос вашего кода на Aspose.PDF для Java 2.5.0
type: docs
weight: 10
url: ru/java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

В этой статье мы попытались выделить некоторые области из существующего кода Aspose.PDF для Java, чтобы сделать его совместимым с последней версией релиза.

{{% /alert %}}

## Подробности

С выпуском Aspose.PDF для Java 2.5.0 произошло много изменений в структуре API и конструкции классов. Большинство названий членов классов обновлены, некоторые существующие члены классов удалены, а также добавлено несколько методов и свойств в существующие классы. Чтобы дать вам краткий обзор изменений, мы рассмотрим следующий простой код, основанный на версиях Aspose.PDF для Java, опубликованных ранее версии 2.5.0.

В этом простом коде мы добавим гиперссылку и ссылку на страницу в том же PDF-документе.

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


//Создаем объект Pdf, вызывая его пустой конструктор

Pdf pdf1 = new Pdf();

//Создаем секцию в объекте Pdf

Section sec1 = pdf1.getSections().add();

//Создаем текстовый абзац с привязкой к секции

Text text1 = new Text(sec1);

//Добавляем текстовый абзац в коллекцию абзацев секции

sec1.getParagraphs().add(text1);

//Добавляем текстовый сегмент в текстовый абзац

Segment segment1 = text1.getSegments().add("this is a local link");

//Устанавливаем текст в текстовом сегменте подчеркнутым

segment1.getTextInfo().setUnderLine(true);


//Устанавливаем тип ссылки текстового сегмента как Local

//Назначаем id нужного абзаца в качестве целевого id для текстового сегмента

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//Создаем текстовый абзац, который будет связан с текстовым сегментом

Text text3 = new Text(sec1,"product 1 info ...");

//Добавляем текстовый абзац в коллекцию абзацев секции

sec1.getParagraphs().add(text3);

//Устанавливаем этот абзац первым, чтобы он отображался на отдельной

//странице в документе

text3.setFirstParagraph(true);

//Устанавливаем id этого текстового сегмента как "product1"

text3.setID("product1"); 


// сохраняем файл PDF

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```
```


Когда используется версия Aspose.PDF для Java ранее 2.5.0, код может успешно выполняться, и результирующий PDF-документ, содержащий гиперссылку на страницу внутри того же документа, может быть сгенерирован. Но когда тот же код компилируется с версией 2.5.0, вы заметите ряд ошибок, потому что произошли изменения в членах класса, а также некоторые методы в классах были удалены. Теперь давайте начнем с модификации кода для версии 2.5.0

Используйте `import aspose.pdf.*`; вместо `import com.aspose.pdf.elements.*`; чтобы включить пакет.

Для инициализации лицензии, пожалуйста, обновите ваш существующий код с 

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

на 

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo** больше не содержит метод **setUnderLine(...)**. Пожалуйста, попробуйте использовать **TextInfo.setIsUnderline(...)** ** вместо этого **.**

Класс с именем **HyperLinkToLocalPdf** был удален. Поэтому, пожалуйста, обновите ваш существующий код, например

{{% alert color="primary" %}}
**//Установите тип ссылки текстового сегмента на Local**

```java

 //Назначьте id нужного абзаца как целевой id для текстового сегмента

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

на

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

Имя метода **setFirstParagraph** удалено из класса Text.
 Так что для отображения текстового сегмента на новой странице, вам нужно создать новый объект Section и добавить текстовый объект в вновь созданный раздел. Так как по умолчанию каждый раздел отображается на новой странице, нет необходимости вызывать метод типа **sec2.setIsNewPage(true**)**;

## Обновленный метод сохранения

Метод сохранения в классе Pdf, который использовался с объектом FileOutputStream в качестве аргумента, был удален. В новой версии вы можете использовать любой из следующих перегруженных методов сохранения.

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

После внесения всех вышеуказанных изменений, при использовании Aspose.PDF для Java 2.5.0, код будет скомпилирован и выполнен без вывода сообщений об ошибках. Полный обновленный кодовый фрагмент указан ниже.

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//Создаем объект Pdf, вызывая его пустой конструктор

Pdf pdf1 = new Pdf();

//Создаем раздел в объекте Pdf

Section sec1 = pdf1.getSections().add();

//Создаем текстовый абзац с ссылкой на раздел

Text text1 = new Text(sec1);

//Добавляем текстовый абзац в коллекцию абзацев раздела

sec1.getParagraphs().add(text1);

//Добавляем текстовый сегмент в текстовый абзац

Segment segment1 = text1.getSegments().add("this is a local link");

//Устанавливаем текст в текстовом сегменте как подчеркнутый

segment1.getTextInfo().setIsUnderline(true);


//Устанавливаем тип ссылки текстового сегмента как Local

//Назначаем id желаемого абзаца в качестве целевого id для текстового сегмента

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// добавляем новый раздел, который будет содержать текстовый объект с ID "Product 1"

Section sec2 = pdf1.getSections().add();

//Создаем текстовый абзац, который будет связан с текстовым сегментом

Text text3 = new Text(sec1,"product 1 info ...");

//Добавляем текстовый абзац в коллекцию абзацев раздела

sec2.getParagraphs().add(text3);

//Устанавливаем id этого текстового сегмента как "product1"

text3.setID("product1");


// сохраняем файл PDF

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## Заключение

В вышеуказанной теме мы объяснили некоторые из классов и методов, которые были изменены в новом выпуске. Для получения полного списка всех классов и их членов, пожалуйста, посетите [Aspose.PDF для Java API Reference](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)

Чтобы узнать больше об Aspose и его продуктах, пожалуйста, нажмите здесь <http://www.aspose.com/>