<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="2.0">
    
    <xsl:output method="xhtml" indent="yes" encoding="UTF-8"/>
    
    <xsl:template match="/">
        <xsl:result-document href="pr.html">
            <html>
                <head>
                    <title>Manifesto</title>
                    <meta charset="UTF-8"/>
                </head>
                <body bgcolor="#ebfaef">
                    <h1 align="center" style="color:#08540b">Manifesto</h1>
                    <xsl:apply-templates/>
                </body>
            </html>
        </xsl:result-document>
    </xsl:template>
    
    <xsl:template match="meta">
        <div style="margin:1cm">
            <table>
                <tr>
                    <th align="left">Key Name: </th><td><xsl:value-of select="keyname"/></td>
                </tr>
                <tr>
                    <th align="left">Title: </th><td><xsl:value-of select="title"/></td>
                </tr>
                <tr>
                    <th align="left">Subtitle: </th><td><xsl:value-of select="subtitle"/></td>
                </tr>
                <tr>
                    <th align="left">Begin Date: </th><td><xsl:value-of select="bdate"/></td>
                </tr>
                <tr>
                    <th align="left">End Date: </th><td><xsl:value-of select="edate"/></td>
                </tr>
            </table>
            <h2 style="color:#08540b">Supervisor</h2>
            <table>
                <tr>
                    <th align="left">Name: </th><td><xsl:value-of select="supervisor/name"/></td>
                </tr>
                <tr>
                    <th align="left">Email: </th><td><xsl:value-of select="supervisor/email"/></td>
                </tr>
                <tr>
                    <th align="left">Homepage: </th><td><a href="{supervisor/homepage}"><xsl:value-of select="supervisor/homepage"/></a></td>
                </tr>
            </table>
        </div>
    </xsl:template>
    
    <xsl:template match="workteam">
        <div style="margin:1cm">
            <h2 style="color:#08540b">Workteam</h2>
            <table>
                <tr>
                    <th align="left">Identifier: </th><td><xsl:value-of select="member/identifier"/></td>
                </tr>
                <tr>
                    <th align="left">Name: </th><td><xsl:value-of select="member/name"/></td>
                </tr>
                <tr>
                    <th align="left">Email: </th><td><xsl:value-of select="member/email"/></td>
                </tr>
                <tr>
                    <th align="left">Photo: </th>
                    <td>
                        <img width="150" height="150">
                            <xsl:attribute name="src">
                                <xsl:value-of select="member/photo/@path"/>
                            </xsl:attribute>
                        </img>
                    </td>
                </tr>
            </table>
        </div>
    </xsl:template>
    
    <xsl:template match="abstract">
        <div style="margin:1cm">
            <h2 style="color:#08540b">Abstract</h2>
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    
    <xsl:template match="p">
        <div>
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    
    <xsl:template match="i">
        <i><xsl:apply-templates/></i>
    </xsl:template>
    
    <xsl:template match="deliverables">
        <div style="margin:1cm">
            <h2 style="color:#08540b">Deliverables</h2>
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    
    <xsl:template match="deliverable">
        <div>
            <a href="{@path}"><xsl:value-of select="."/></a>
        </div>
    </xsl:template>
    
    <xsl:template match="xref">
        <a href="{@url}"><xsl:value-of select="."/></a>
    </xsl:template>
    
</xsl:stylesheet>