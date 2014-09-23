// http://code.google.com/p/lxyppc-snake/source/browse/trunk/crccrash/crccrash.c
/**
  all these code is based on 
    http://www.pediy.com/bbshtml/BBS6/pediy6937.htm

  and 
    http://hi.baidu.com/fenjianren/blog/item/5e5967e92101143cb80e2d29.html

  Thanks
   lxyppc
 */

#include<stdio.h>
#include<string.h>
unsigned long crc32_table[256]={
0x00000000,0x77073096,0xEE0E612C,0x990951BA,0x076DC419,0x706AF48F,0xE963A535,0x9E6495A3,
0x0EDB8832,0x79DCB8A4,0xE0D5E91E,0x97D2D988,0x09B64C2B,0x7EB17CBD,0xE7B82D07,0x90BF1D91,
0x1DB71064,0x6AB020F2,0xF3B97148,0x84BE41DE,0x1ADAD47D,0x6DDDE4EB,0xF4D4B551,0x83D385C7,
0x136C9856,0x646BA8C0,0xFD62F97A,0x8A65C9EC,0x14015C4F,0x63066CD9,0xFA0F3D63,0x8D080DF5,
0x3B6E20C8,0x4C69105E,0xD56041E4,0xA2677172,0x3C03E4D1,0x4B04D447,0xD20D85FD,0xA50AB56B,
0x35B5A8FA,0x42B2986C,0xDBBBC9D6,0xACBCF940,0x32D86CE3,0x45DF5C75,0xDCD60DCF,0xABD13D59,
0x26D930AC,0x51DE003A,0xC8D75180,0xBFD06116,0x21B4F4B5,0x56B3C423,0xCFBA9599,0xB8BDA50F,
0x2802B89E,0x5F058808,0xC60CD9B2,0xB10BE924,0x2F6F7C87,0x58684C11,0xC1611DAB,0xB6662D3D,
0x76DC4190,0x01DB7106,0x98D220BC,0xEFD5102A,0x71B18589,0x06B6B51F,0x9FBFE4A5,0xE8B8D433,
0x7807C9A2,0x0F00F934,0x9609A88E,0xE10E9818,0x7F6A0DBB,0x086D3D2D,0x91646C97,0xE6635C01,
0x6B6B51F4,0x1C6C6162,0x856530D8,0xF262004E,0x6C0695ED,0x1B01A57B,0x8208F4C1,0xF50FC457,
0x65B0D9C6,0x12B7E950,0x8BBEB8EA,0xFCB9887C,0x62DD1DDF,0x15DA2D49,0x8CD37CF3,0xFBD44C65,
0x4DB26158,0x3AB551CE,0xA3BC0074,0xD4BB30E2,0x4ADFA541,0x3DD895D7,0xA4D1C46D,0xD3D6F4FB,
0x4369E96A,0x346ED9FC,0xAD678846,0xDA60B8D0,0x44042D73,0x33031DE5,0xAA0A4C5F,0xDD0D7CC9,
0x5005713C,0x270241AA,0xBE0B1010,0xC90C2086,0x5768B525,0x206F85B3,0xB966D409,0xCE61E49F,
0x5EDEF90E,0x29D9C998,0xB0D09822,0xC7D7A8B4,0x59B33D17,0x2EB40D81,0xB7BD5C3B,0xC0BA6CAD,
0xEDB88320,0x9ABFB3B6,0x03B6E20C,0x74B1D29A,0xEAD54739,0x9DD277AF,0x04DB2615,0x73DC1683,
0xE3630B12,0x94643B84,0x0D6D6A3E,0x7A6A5AA8,0xE40ECF0B,0x9309FF9D,0x0A00AE27,0x7D079EB1,
0xF00F9344,0x8708A3D2,0x1E01F268,0x6906C2FE,0xF762575D,0x806567CB,0x196C3671,0x6E6B06E7,
0xFED41B76,0x89D32BE0,0x10DA7A5A,0x67DD4ACC,0xF9B9DF6F,0x8EBEEFF9,0x17B7BE43,0x60B08ED5,
0xD6D6A3E8,0xA1D1937E,0x38D8C2C4,0x4FDFF252,0xD1BB67F1,0xA6BC5767,0x3FB506DD,0x48B2364B,
0xD80D2BDA,0xAF0A1B4C,0x36034AF6,0x41047A60,0xDF60EFC3,0xA867DF55,0x316E8EEF,0x4669BE79,
0xCB61B38C,0xBC66831A,0x256FD2A0,0x5268E236,0xCC0C7795,0xBB0B4703,0x220216B9,0x5505262F,
0xC5BA3BBE,0xB2BD0B28,0x2BB45A92,0x5CB36A04,0xC2D7FFA7,0xB5D0CF31,0x2CD99E8B,0x5BDEAE1D,
0x9B64C2B0,0xEC63F226,0x756AA39C,0x026D930A,0x9C0906A9,0xEB0E363F,0x72076785,0x05005713,
0x95BF4A82,0xE2B87A14,0x7BB12BAE,0x0CB61B38,0x92D28E9B,0xE5D5BE0D,0x7CDCEFB7,0x0BDBDF21,
0x86D3D2D4,0xF1D4E242,0x68DDB3F8,0x1FDA836E,0x81BE16CD,0xF6B9265B,0x6FB077E1,0x18B74777,
0x88085AE6,0xFF0F6A70,0x66063BCA,0x11010B5C,0x8F659EFF,0xF862AE69,0x616BFFD3,0x166CCF45,
0xA00AE278,0xD70DD2EE,0x4E048354,0x3903B3C2,0xA7672661,0xD06016F7,0x4969474D,0x3E6E77DB,
0xAED16A4A,0xD9D65ADC,0x40DF0B66,0x37D83BF0,0xA9BCAE53,0xDEBB9EC5,0x47B2CF7F,0x30B5FFE9,
0xBDBDF21C,0xCABAC28A,0x53B39330,0x24B4A3A6,0xBAD03605,0xCDD70693,0x54DE5729,0x23D967BF,
0xB3667A2E,0xC4614AB8,0x5D681B02,0x2A6F2B94,0xB40BBE37,0xC30C8EA1,0x5A05DF1B,0x2D02EF8D
};

unsigned long combine(unsigned char a4,unsigned char a3,unsigned char a2,unsigned char a1)
{ //返回以从高到低4个字节为a4,a3,a2,a1的32位数
    unsigned long tmp;
    tmp=(unsigned long)a4;
    tmp=(tmp<<24);
    tmp=tmp^((unsigned long)a3<<16&0x0FFFFFF);
    tmp=tmp^((unsigned long)a2<<8&0x0FFFF);
    tmp=tmp^((unsigned long)a1);
    return tmp;
}
unsigned char UL_1(unsigned long x)
{//取得32位数ABCD的低8位，即D
return (unsigned char)(x&0x0FF);
}
unsigned char UL_2(unsigned long x)
{//取得32位数ABCD的C
return (unsigned char)(x>>8&0x0FF);
}
unsigned char UL_3(unsigned long x)
{//取得32位数ABCD的B
return (unsigned char)(x>>16&0x0FF);
}
unsigned char UL_4(unsigned long x)
{//取得32位数ABCD的高8位，即A
return (unsigned char)(x>>24&0x0FF);
}

//定义4个函数F(x),G(x),H(x),I(x)分别表示以x为索引查表,取出来的DWORD的从高位到低位的4个字节
unsigned char F(unsigned char x)
{
    return UL_4(crc32_table[x]);
}
unsigned char G(unsigned char x)
{
    return UL_3(crc32_table[x]);
}
unsigned char H(unsigned char x)
{
    return UL_2(crc32_table[x]);
}
unsigned char I(unsigned char x)
{
    return UL_1(crc32_table[x]);
}

unsigned char RF(unsigned char x)
{//F函数的逆函数
    unsigned char j;
    for(j=0;j<=0xFF;j++)
    {
      if(UL_4(crc32_table[j]) == x) break;
    }
    return j;
}

unsigned long solve_ABCD(unsigned long value,unsigned long final)
{
    unsigned char p,o,n,m,a,b,c,d,W,X,Y,Z,A,B,C,D;
    unsigned long last4;

    W=UL_4(final);
    X=UL_3(final);
    Y=UL_2(final);
    Z=UL_1(final);

    p=RF(W);
    o=RF(X^G(p));
    n=RF(Y^G(o)^H(p));
    m=RF(Z^G(n)^H(o)^I(p));

    a=UL_4(value);
    b=UL_3(value);
    c=UL_2(value);
    d=UL_1(value);

    D=m^d;
    C=n^c^I(m);
    B=o^b^H(m)^I(n);
    A=p^a^G(m)^H(n)^I(o);

    last4=combine(A,B,C,D);
    return last4;
}

unsigned long crc32_crash(unsigned long former,unsigned long final)
{/*在经过很多轮后效验值为ABCD,接着要效验的数据是abcd,效验后的结果为WXYZ,其中4轮的查表索引值为mnop
(单个字母都表示一个字节),因此关键就是由(former)ABCD+(final)WXYZ推出最后4个字节(last4)abcd*/
    unsigned char p,o,n,m,a,b,c,d,W,X,Y,Z,A,B,C,D;
    unsigned long last4;
    W=UL_4(final);
    X=UL_3(final);
    Y=UL_2(final);
    Z=UL_1(final);

    A=UL_4(former);
    B=UL_3(former);
    C=UL_2(former);
    D=UL_1(former);

    p=RF(W);
    o=RF(X^G(p));
    n=RF(Y^G(o)^H(p));
    m=RF(Z^G(n)^H(o)^I(p));

    d=m^D;
    c=n^C^I(m);
    b=o^B^H(m)^I(n);
    a=p^A^G(m)^H(n)^I(o);
    last4=combine(a,b,c,d);
    return last4;
}
unsigned long crc32(const unsigned char* p,int len)
{
    int i;
    const unsigned char* str = (const unsigned char*)p;
     unsigned long crc=0x0FFFFFFFF;
     for (i=0;i<len;i++)
       crc = crc32_table[(crc & 0x0ff) ^ (unsigned char)str[i]] ^ (crc >> 8);
     crc=~crc;
     return crc;
}

void displaydata(const void* p, int len, const char* desc)
{
    int i = 0;
    const unsigned char* buf = (const unsigned char*)p;
    if(desc)printf("%s\n",desc);
    for(i=0;i<len;i++){
        printf("%02X ",buf[i]);
        if((i&0xf) == 0xf){
            printf("\n");
        }
    }
    printf("\n");
}

void crash_crc32_at(void* p, int len, unsigned long result, int position)
{
    unsigned long final;
    unsigned long former;
    unsigned long value;
    if(len&2)return;        // must 4 bytes aligned
    if(position&2)return;   // must 4 bytes aligned
    if(position > len -4) return;  // over flow
    final = ~result;
    former = ~crc32(p,position);
    len-=4;
    while(position<len){
        value = *(unsigned long*)((unsigned char*)p+len);
        final = solve_ABCD(value,final);
        len -=4;
    }
    value = *(unsigned long*)((unsigned char*)p+position);
    final = crc32_crash(former,final);
    ((unsigned char*)p)[position+0] =  UL_1(final);
    ((unsigned char*)p)[position+1] =  UL_2(final);
    ((unsigned char*)p)[position+2] =  UL_3(final);
    ((unsigned char*)p)[position+3] =  UL_4(final);
};

void main()
{
    int i;
    for(i=0;i<32;i+=4){
        unsigned char data[32] = {0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f,
                                  0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,};
        unsigned int crcresult = 0x12345678;
        printf("\nReplace data at %d, make result to 0x%08x\n",i,crcresult);
        displaydata(data,32,"org data");
        crash_crc32_at(data,32,crcresult,i);
        displaydata(data,32,"crash data");
        printf("crc result is 0x%08x\n", (unsigned int)crc32(data,32));
    }
#if 0

    unsigned long former,last4,final,crc,former0;
    unsigned char str[20]={0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07};
    int len = 8;
    unsigned long crcresult = crc32(str,len);
    unsigned long value = 0;
    displaydata(str,len,"org data");
    displaydata(&crcresult,4,"crc value");
    printf("\n\nlet's makte crc result to 0x12345678 ...\n");
    former = ~crcresult;
    final = ~0x12345678;
    last4=crc32_crash(former,final);
    str[len+0] = UL_1(last4);
    str[len+1] = UL_2(last4);
    str[len+2] = UL_3(last4);
    str[len+3] = UL_4(last4);

    displaydata(&str,len+4,"new data is");
    crcresult = crc32(str,len+4);
    displaydata(&crcresult,4,"crc value");


    printf("\n\nlet's change the middle value (replace the 0xffs)....\n");
    memcpy(str+len,str+len-4,5);
    memset(str+len-4,0xff,4);
    displaydata(str,len+4,"org data");
    value = *(unsigned long*)(str+len);
    final = ~0x12345678;
    former = solve_ABCD(value,final);
    former0 = ~crc32(str,len-4);
    last4=crc32_crash(former0,former);

    str[len+0-4] = UL_1(last4);
    str[len+1-4] = UL_2(last4);
    str[len+2-4] = UL_3(last4);
    str[len+3-4] = UL_4(last4);
    displaydata(&str,len+4,"new data is");
    crcresult = crc32(str,len+4);
    displaydata(&crcresult,4,"crc value");

    crash_crc32_at(str,len+4,0x12345678,len-4);
    displaydata(&str,len+4,"new data is");
#endif
}



