---
title: Объединение документов PDF
type: docs
weight: 10
url: ru/java/concatenate-pdf-documents/
description: Этот раздел объясняет, как объединять PDF-документы с использованием com.aspose.pdf.facades и класса PdfFileEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Объединение PDF файлов с использованием путей к файлам (Facades)

метод concatenate класса [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) может быть использован для объединения двух PDF файлов. Метод concatenate позволяет передать три параметра: первый входной PDF, второй входной PDF и выходной PDF. Итоговый выходной PDF содержит оба входных PDF файла.

Следующий фрагмент кода показывает, как объединить PDF файлы, используя пути к файлам.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // Создать объект PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Объединить файлы
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


В некоторых случаях, когда существует множество контуров, пользователи могут отключить их, установив **CopyOutlines** в значение false и улучшив таким образом производительность объединения.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // Создаем объект PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Объединяем файлы
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## Объединение нескольких PDF файлов с использованием MemoryStreams

Метод [Concatenate]https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) класса [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) принимает исходные PDF файлы и целевой PDF файл в качестве параметров.
 Эти параметры могут быть либо путями к PDF-файлам на диске, либо MemoryStreams. Теперь, для этого примера, мы сначала создадим два файловых потока для чтения PDF-файлов с диска. Затем мы преобразуем эти файлы в массивы байтов. Эти массивы байтов PDF-файлов будут преобразованы в MemoryStreams. Как только мы получим MemoryStreams из PDF-файлов, мы сможем передать их в метод объединения и объединить в один выходной файл.

Следующий фрагмент кода показывает, как объединить несколько PDF-файлов, используя MemoryStreams:

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // Создаем два файловых потока для чтения PDF-файлов
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // Создаем массивы байтов для хранения содержимого PDF-файлов
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // Читаем содержимое PDF-файлов в массивы байтов
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Теперь сначала преобразуем массивы байтов в MemoryStreams, а затем объединим эти потоки
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // Создаем экземпляр класса PdfFileEditor для объединения потоков
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // Объединяем оба входных MemoryStreams и сохраняем в выходной MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Преобразуем MemoryStream обратно в массив байтов
                        byte[] data = pdfStream.ToArray();
                        // Создаем FileStream для сохранения выходного PDF-файла
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // Записываем содержимое массива байтов в выходной файловый поток
                        output.Write(data, 0, data.Length);
                        // Закрываем выходной файл
                        output.Close();
                    }
                }
            }
            // Закрываем входные файлы
            fs1.Close();
            fs2.Close();
        }
```

## Объединение массива PDF файлов с использованием путей к файлам (Фасады)

Если вы хотите объединить несколько PDF файлов, вы можете использовать перегрузку метода объединения, которая позволяет передать массив путей к PDF файлам. Окончательный результат сохраняется как объединенный файл, созданный из всех файлов в массиве.

Следующий фрагмент кода показывает, как объединить массив PDF файлов, используя пути к файлам.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // Создание объекта PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Массив файлов
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // Объединение файлов
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## Объединение массива PDF файлов с использованием потоков (Фасады)

Объединение массива PDF файлов не ограничивается только файлами, находящимися на диске.
 Вы также можете объединить массив PDF файлов из потоков. Если вы хотите объединить несколько PDF файлов, вы можете использовать соответствующую перегрузку метода Concatenate. Сначала вам нужно создать массив входных потоков и один поток для выходного PDF, а затем вызвать метод Concatenate. Результат будет сохранен в выходном потоке.

Следующий фрагмент кода показывает, как объединить массив PDF файлов, используя потоки.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // Создать объект PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Массив потоков
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // Выходной поток
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // Объединить файл
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## Конкатенация PDF форм и сохранение уникальных имен полей

Класс [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) в пространстве имен [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) предлагает возможность конкатенации PDF файлов.
 Теперь, если PDF файлы, которые необходимо объединить, содержат поля формы с одинаковыми именами, Aspose.PDF предоставляет возможность сохранить поля в результирующем PDF-файле уникальными, и также можно указать суффикс, чтобы сделать имена полей уникальными. Метод [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) класса PdfFileEditor, установленный в значение true, сделает имена полей уникальными при объединении форм PDF. Также метод [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) класса PdfFileEditor может быть использован для указания пользовательского формата суффикса, который добавляется к имени поля, чтобы сделать его уникальным при объединении форм. Эта строка должна содержать подстроку %NUM%, которая будет заменена на числа в результирующем файле.

Пожалуйста, ознакомьтесь с следующим простым фрагментом кода для достижения этой функциональности.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // Установить пути к входным и выходным файлам

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // Создать экземпляр объекта PdfFileEditor
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // Чтобы сохранить уникальный идентификатор поля для всех полей
                KeepFieldsUnique = true,
                // Формат суффикса, который добавляется к имени поля, чтобы сделать его уникальным при объединении форм.
                UniqueSuffix = "_%NUM%"
            };

            // Объединить файлы в результирующий PDF-файл
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## Объединение Вставка пустой страницы

После объединения файлов PDF мы можем вставить пустую страницу в начало документа, на которой можно создать оглавление. Чтобы выполнить это требование, мы можем загрузить объединенный файл в объект Document и вызвать метод Page.Insert(…) для вставки пустой страницы.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // Создаем объект PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // Объединяем файлы
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```