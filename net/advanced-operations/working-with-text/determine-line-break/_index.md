---
title: Determine Line Break
linktitle: Determine Line Break
type: docs
weight: 70
url: /net/determine-line-break/
description: Learn more about how to determinate a line break of multi-line TextFragment.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Track Line Breaking of Multi-Line TextFragment

Aspose.PDF for .NET offers logging (tracking) background processing (line breaking) of multi-line text fragments in text adding scenarios. You can use the [GetNotifications](https://apireference.aspose.com/pdf/net/aspose.pdf/page/methods/getnotifications)() method of [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) Class as follows, in order to track line breaking of text fragment:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

for (int i = 0; i < 4; i++)
{
    TextFragment text = new TextFragment("Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.");
    text.TextState.FontSize = 20;
    page.Paragraphs.Add(text);
}
doc.Save(dataDir + "DetermineLineBreak_out.pdf");

string notifications = doc.Pages[1].GetNotifications();
File.WriteAllText(dataDir + "notifications_out.txt", notifications);
```
