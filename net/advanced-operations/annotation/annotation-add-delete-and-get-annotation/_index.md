---
title: Add, Delete and Get Annotation 
type: docs
weight: 10
url: /net/add-delete-and-get-annotation/
---
# Add, Delete and Get Annotation

## Add Annotation in existing PDF file
Annotations are contained by the [Annotations](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations) collection of a particular Page. This collection contains the annotations for that individual page only; every page has its own Annotations collection.

To add an annotation to a particular page, add it to that page’s Annotations collection with the [Add](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add) method.

1. First, create an annotation that you want to add to the PDF.
1. Then open the input PDF.
1. Add the annotation to the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s Annotations collection.

The following code snippet shows you how to add an annotation in a PDF page.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// Create annotation
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "Sample Annotation Title";
textAnnotation.Subject = "Sample Subject";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "Sample contents for the annotation";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;
           
Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);
           
// Add annotation in the annotations collection of the page
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// Save output file
pdfDocument.Save(dataDir);
```
## Free text annotation

### Set Callout Property for FreeTextAnnotation
For a more flexible configuration of annotation in the PDF document, Aspose.PDF for .NET provides Callout property of FreeTextAnnotation class which allows specifying Array of point of callout line. The following code snippet show, how to use this functionality:
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### Set Callout Property for XFDF File
If you use import from XFDF file please use callout-line name instead just Callout. The following code snippet shows, how to use this functionality:
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document( dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```
The following method is being used to CreateXfdf:
```
 /// <summary>

/// Create XFDF

/// </summary>

/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)

{

    pXfdf.Append("<freetext");

    pXfdf.Append(" page=\"0\"");

    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");

    pXfdf.Append(" intent=\"FreeTextCallout\"");

    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");

    pXfdf.Append(" tail=\"OpenArrow\"");

    pXfdf.AppendLine(">");

    pXfdf.Append("<contents-richtext><body ");

    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");

    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");

    pXfdf.Append("</body></contents-richtext>");

    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");

    pXfdf.AppendLine("</freetext>");

}
```
### Invisible Annotation
Sometimes, it is necessary to create a watermark that isn’t visible in the document when viewing it but should be visible when the document is printed. Use annotation flags for this purpose. The following code snippet shows how.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// Save output file
doc.Save(dataDir);
```
## Adding InkAnnotation
The [InkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) represents freehand scribble composed of one or more disjoint points. Please try using the following code snippet to add InkAnnotation in PDF document.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page pdfPage = doc.Pages.Add();
System.Drawing.Rectangle drect = new System.Drawing.Rectangle();
drect.Height = (int)pdfPage.Rect.Height;
drect.Width = (int)pdfPage.Rect.Width;
drect.X = 0;
drect.Y = 0;
Aspose.Pdf.Rectangle arect = Aspose.Pdf.Rectangle.FromRect(drect);
IList<Point[]> inkList = new List<Point[]>();
Aspose.Pdf.Point[] arrpt = new Aspose.Pdf.Point[3];
inkList.Add(arrpt);
arrpt[0] = new Aspose.Pdf.Point(100, 800);
arrpt[1] = new Aspose.Pdf.Point(200, 800);
arrpt[2] = new Aspose.Pdf.Point(200, 700);
InkAnnotation ia = new InkAnnotation(pdfPage, arect, inkList);
ia.Title = "XXX";
ia.Color = Aspose.Pdf.Color.LightBlue; // (GetColorFromString(stroke.InkColor));
ia.CapStyle = CapStyle.Rounded;
Border border = new Border(ia);
border.Width = 25;
ia.Opacity = 0.5;
pdfPage.Annotations.Add(ia);

dataDir = dataDir + "AddlnkAnnotation_out.pdf";
// Save output file
doc.Save(dataDir);
```
## Set Line width of InkAnnotation
The width of [InkAnnottion](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) can be changed using LineInfo and Border objects.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Title";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// Save output file
doc.Save(dataDir);
```
## Adding WatermarkAnnotation
You can add Watermark Text using [WatermarkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation) at a specific position of the PDF page. The opacity of Watermark can also be controlled by using opacity property. Please check the following code snippet to add WatermarkAnnotation.

C#
```
 //Load a Document

Aspose.PDF.Document doc = new Aspose.PDF.Document("source.pdf");

//Load Page object to add Annotation

Page page = doc.Pages[1];

//Create Annotation

WatermarkAnnotation wa = new WatermarkAnnotation(page, new Aspose.PDF.Rectangle(100, 500, 400, 600));

//Add annotaiton into Annotation collection of Page

page.Annotations.Add(wa);

//Create TextState for Font settings

Aspose.PDF.Text.TextState ts = new Aspose.PDF.Text.TextState();

ts.ForegroundColor = Aspose.PDF.Color.Blue;

ts.Font = FontRepository.FindFont("Times New Roman");

ts.FontSize = 32;

//Set opacity level of Annotaiton Text

wa.Opacity = 0.5;

//Add Text in Annotation

wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

//Save the Docuemnt

doc.Save("Output.pdf");
```
## Adding RichMediaAnnotation
When you need to add an external video link in PDF document, you can use [MovieAnnotaiton](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation). However, when there is a requirement to embed media inside PDF document, you need to use [RichMediaAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation). This annotation allows to embed media file within PDF document and set video/audio player, implemented as flash application. Due to license restriction, we can not include third-party flash scripts in our product, so you should provide your script for playing video or audio. You should provide a flash application code. For example, you can use videoplayer.swf and audioplayer.swf which are distributed with Adobe Acrobat and may be found in Multimedia Skins/Players subfolder in Acrobat folder. Another choice is using StrobeMediaPLayback.swf player or any other video player implemented in flash.

The following methods/properties of RichMediaAnnotation class can be used.

- Stream CustomPlayer { set; }: Allows setting player used to play video.
- string CustomFlashVariables { set; }: Allows to set variables that are passed to flash application. This line is set of “key=value” pairs which are separated with ‘&';
- void AddCustomData(strig name, Stream data):  Add additional data for the player. For example source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}:  Event activates player; possible values are Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Set video/audio data to be played
- void Update():  Create a data structure of the annotation. This method should be called last
- void SetPoster(Stream): Set poster of the video i.e. picture shown when the player is not active

## Embed Video File
Embedding video file can be achieved using the following sample code.

C#
```
 string myDir = "C:/Temp/";


Aspose.PDF.Document doc = new Aspose.PDF.Document();

Page page = doc.Pages.Add();

RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.PDF.Rectangle(100,500, 300, 600));

//here we should specify stream containing code of the video player

rma.CustomPlayer = new FileStream(@"C:\Adobe\Acrobat 11.0\Acrobat\MultimediaSkins\Players\Videoplayer.swf",FileMode.Open,FileAccess.Read);

//give name to video data. This data will be embedded into document with this name and referenced from flash variables by this name. 

//videoName should not contain path to the file; this is rather "key" to access data inside of the PDF document

string videoName = "VideoTutorial.mp4";

//also we use skin for video player

string skinName = "SkinOverAllNoFullNoCaption.swf";

//compose flash variables line for player. please note that different players may have different format of the flash variables line. Refer to documentation for your player.

rma.CustomFlashVariables = String.Format("source={0}&skin={1}", "VideoTutorial.mp4", skinName);

//add skin code. 

rma.AddCustomData(skinName,new FileStream(@"C:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\Multimedia Skins\SkinOverAllNoFullNoCaption.swf",FileMode.Open, FileAccess.Read));

//set poster for video

rma.SetPoster(new FileStream(myDir + "barcode.jpg",FileMode.Open, FileAccess.Read));

Stream fs = new FileStream(myDir + videoName, FileMode.Open, FileAccess.Read);

//set video content

rma.SetContent(videoName, fs);

//set type of the content (video)

rma.Type = RichMediaAnnotation.ContentType.Video;

//active player by click

rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

//update annotation data. This method should be called after all assignments/setup. This method initializes data structure of the annotation and embeds required data. 

rma.Update();

//add annotation on the page.

page.Annotations.Add(rma);

doc.Save(myDir + "Output.pdf");
```

## Embed Audio File
Embedding audio files can be achieved using the following sample code.

C#
```
 Aspose.PDF.Document

doc = new Aspose.PDF.Document();

Page page = doc.Pages.Add();

//give name to audio data. This data will be embedded into document with this name and referenced from flash variables by this name. 

string audioName = "test_cbr.mp3";

RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.PDF.Rectangle(100,650, 300, 670));

Stream fs = new FileStream(myDir+audioName, FileMode.Open, FileAccess.Read);

//here we should specify stream containing code of the audio player

rma.CustomPlayer = new FileStream(@"C:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\MultimediaSkins\Players\Audioplayer.swf", FileMode.Open,

FileAccess.Read);

//compose flash variables line for player. please note that different players may have different format of the flash variables line. Refer to documentation for your player.

rma.CustomFlashVariables = String.Format("source={0}", "test_cbr.mp3");

//active player on page open event

rma.ActivateOn = RichMediaAnnotation.ActivationEvent.PageOpen;

//set audio content

rma.SetContent(audioName, fs);

//set type of the content (audio)

rma.Type = RichMediaAnnotation.ContentType.Audio;

//update annotation data. This method should be called after all assignments/setup. This method initializes data structure of the annotation and embeds required data. 

rma.Update();

//add annotation on the page.

page.Annotations.Add(rma);

doc.Save(myDir+"39606-2.pdf");
```

## Add SWF File Annotation to PDF Document
Annotations in a PDF document are contained in a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s Annotations collection. This collection contains all annotations for that individual page only: every page has its own Annotations collection. To add an annotation to a particular page, add it to that page’s Annotations collection using the Add method. Use the [ScreenAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) class in the Aspose.PDF.InteractiveFeatures.Annotations namespace to include SWF files as annotations in a PDF document instead.

ScreenAnnotation takes three arguments:

1. The page you are adding the annotation to,
1. A Rectangle object which defines the area in the PDF where the annotation will be displayed, and
1. The path to the SWF multimedia file.

To add an SWF file as an annotation:

1. First, create an instance of ScreenAnnotation.
1. Then add it to the page’s Annotations collection using the Add method.
The following code snippet shows you how to add SWF annotation in a PDF page.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open the PDF document
Document doc = new Document(dataDir + "AddSwfFileAsAnnotation.pdf");
            
// Get reference of the page to which you need to add the annotation
Page page = doc.Pages[1];
            
// Create ScreenAnnotation object with .swf multimedia file as an argument
ScreenAnnotation annotation = new ScreenAnnotation(page, new Aspose.Pdf.Rectangle(0, 400, 600, 700), dataDir + "input.swf");
           
// Add the annotation to annotations collection of page
page.Annotations.Add(annotation);

dataDir = dataDir + "AddSwfFileAsAnnotation_out.pdf";
// Save the update PDF document with annotation
doc.Save(dataDir);
```
## Delete All Annotations from a Page of a PDF File
A [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s [AnnotationCollection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection contains all the annotations for that particular page. To delete all the annotations from a page, call the *Delete* method of the AnnotationCollectoin collection.

The following code snippet shows you how to delete all the annotations from a particular page.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// Delete particular annotation
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```
## Delete a Particular Annotation from the PDF File
>You can check the quality of Aspose.PDF and get the results online at this link:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

Aspose.PDF allows you to remove a particular Annotation from PDF file. This topic explains how.

To delete a particular annotation from a PDF, call the [AnnotationCollection collection’s Delete method](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). This collection belongs to the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object. The Delete method requires the index of the annotation you want to delete. Then, save the updated PDF file. The following code snippet shows how to delete a particular annotation.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// Delete particular annotation
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```
## Get All Annotations from the Page of a PDF Document
Aspose.PDF allows you to get annotations from an entire document, or from a given page. To get all annotations from the page in a PDF document, loop through the [AnnotationCollection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection of desired page resources. The following code snippet shows you how to get all the annotations of a page.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// Loop through all the annotations
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // Get annotation properties
    Console.WriteLine("Title : {0} ", annotation.Title);
    Console.WriteLine("Subject : {0} ", annotation.Subject);
    Console.WriteLine("Contents : {0} ", annotation.Contents);                
}
```
Please note that to get all annotations from the whole PDF, you have to loop through the document’s PageCollection Class collection before navigating through the AnnotationCollection class collection. You can get each annotation of the collection in a base annotation type called MarkupAnnotation Class and then show its properties.

## Get Particular Annotation from a PDF File
Annotations are associated with individual pages and stored in a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s [AnnotationCOllection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection. To get a particular annotation, specify its index. This returns an [Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) object which needs to be cast to a particular annotation type, for example [TextAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/textannotation). The following code snippet shows how to get a particular annotation and its properties.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// Get particular annotation
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];
            
// Get annotation properties
Console.WriteLine("Title : {0} ", textAnnotation.Title);
Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
```
## Get Resource of Annotation
Aspose.PDF allows you to get a resource of annotation from an entire document, or from a given page. The following code snippet shows you how to get the resource of annotation as FileSpecification object of input PDF file.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document doc = new Document(dataDir + "AddAnnotation.pdf");
//Create annotation
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// Save Doucument
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");
// Open document
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");
//Get action of the annotation
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;
//Get rendition of the rendition action
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;
//Media Clip 
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
//Data of media are accessible in FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
```