storage=open("Files\\Storage5.bin","wb");
import struct;
data=struct.pack("20s",b"asdadasdasd");
storage.write(data);
print(data);
storage.flush();
storage.close();
storage=open("Files\\Storage5.bin","rb");
data2=struct.unpack("20s",storage.read());
value=data2[0];
print(value.decode("utf-8"));
