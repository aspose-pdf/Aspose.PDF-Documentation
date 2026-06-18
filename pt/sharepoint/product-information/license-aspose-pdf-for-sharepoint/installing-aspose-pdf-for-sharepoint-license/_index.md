---
title: Instalando a Licença Aspose.Pdf para SharePoint
linktitle: Instalando a Licença Aspose.Pdf para SharePoint
type: docs
weight: 10
url: /pt/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Quando estiver satisfeito com sua avaliação, você pode adquirir uma licença para a API PDF SharePoint e seguir as instruções de instalação para aplicá‑la.
---

{{% alert color="primary" %}}

Quando estiver satisfeito com sua avaliação, você pode [adquirir uma licença](https://purchase.aspose.com/buy). Antes de comprar, certifique‑se de que entende e concorda com os termos de assinatura da licença.

{{% /alert %}}

{{% alert color="primary" %}}

A licença será enviada por e‑mail para você após o pagamento do pedido. A licença é um arquivo .zip que contém um pacote de solução SharePoint padrão.

Este arquivo contém:

- Aspose.PDF.SharePoint.License.wsp

Arquivo de pacote de solução SharePoint. A licença Aspose.PDF for SharePoint é empacotada como uma solução SharePoint para facilitar a implantação/retração na fazenda de servidores.

- readme.txt

Instruções de instalação da licença. A instalação da licença é realizada a partir do console do servidor via stsadm.exe. As etapas necessárias para instalar a licença são apresentadas abaixo.

**Nota:** Os caminhos foram omitidos para clareza. Pode ser necessário adicionar o caminho real para stsadm.exe e/ou arquivo de solução ao executá‑los.

1. Execute o stsadm para adicionar a solução ao repositório de soluções do SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Implante a solução em todos os servidores da fazenda:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Execute trabalhos de temporizador administrativos para concluir a implantação imediatamente.

stsadm.exe -o execadmsvcjobs

**Nota:** Você receberá um aviso ao executar a etapa de implantação se o serviço Windows SharePoint Services Administration não estiver iniciado. O Stsadm.exe depende deste serviço e do Windows SharePoint Timer Service para replicar os dados da solução em toda a fazenda. Se esses serviços não estiverem em execução na sua fazenda de servidores, pode ser necessário implantar a licença em cada servidor.


{{% /alert %}}
