import codecs
import config
import fn
import cach

print("swagger   Loading...")

cr=cach.getInstance()


# 写入swagger配置类
source=codecs.open(config.FILEPATH.SWAGGER.value+"SwaggerConfig",'r',encoding='utf8')
lines =source.readlines()
source.close()
fp =codecs.open(cr.get("packagePath")+"config\\"+"SwaggerConfig.java",'w',encoding='utf8')
for s in lines:
    fp.write(s.replace('$JAVANOTE',fn.authNote("Swagger 配置")).replace("$PACKAGE",cr.get("package")))
fp.close()




