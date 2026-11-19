# Generated from grammar/HolocronDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,80,499,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,5,0,90,8,0,10,0,12,0,
        93,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,104,8,1,1,2,1,2,1,
        2,1,2,3,2,110,8,2,1,2,1,2,5,2,114,8,2,10,2,12,2,117,9,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,5,3,126,8,3,10,3,12,3,129,9,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,5,5,138,8,5,10,5,12,5,141,9,5,1,6,1,6,1,6,3,6,146,
        8,6,1,7,1,7,1,7,1,7,3,7,152,8,7,1,8,1,8,1,8,1,8,1,8,5,8,159,8,8,
        10,8,12,8,162,9,8,3,8,164,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,177,8,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,
        11,187,8,11,1,12,1,12,3,12,191,8,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,3,14,202,8,14,1,14,1,14,3,14,206,8,14,1,15,1,15,1,
        16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,3,18,218,8,18,1,19,1,19,3,
        19,222,8,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,5,21,233,
        8,21,10,21,12,21,236,9,21,1,21,1,21,1,21,1,21,1,21,5,21,243,8,21,
        10,21,12,21,246,9,21,3,21,248,8,21,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        281,8,23,1,24,1,24,3,24,285,8,24,1,24,1,24,1,24,5,24,290,8,24,10,
        24,12,24,293,9,24,1,24,3,24,296,8,24,1,25,1,25,1,25,3,25,301,8,25,
        1,25,1,25,1,25,5,25,306,8,25,10,25,12,25,309,9,25,1,25,3,25,312,
        8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,3,26,327,8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,335,8,27,1,
        28,1,28,1,28,1,28,3,28,341,8,28,1,28,5,28,344,8,28,10,28,12,28,347,
        9,28,1,28,3,28,350,8,28,1,28,3,28,353,8,28,1,29,1,29,1,30,1,30,3,
        30,359,8,30,1,30,1,30,3,30,363,8,30,1,30,1,30,3,30,367,8,30,1,30,
        1,30,3,30,371,8,30,1,30,1,30,3,30,375,8,30,1,30,1,30,3,30,379,8,
        30,1,30,1,30,3,30,383,8,30,1,30,1,30,3,30,387,8,30,3,30,389,8,30,
        1,31,1,31,1,31,1,31,5,31,395,8,31,10,31,12,31,398,9,31,1,31,1,31,
        5,31,402,8,31,10,31,12,31,405,9,31,3,31,407,8,31,1,31,1,31,1,32,
        1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,5,33,420,8,33,10,33,12,33,
        423,9,33,1,34,1,34,1,34,1,34,1,34,1,34,5,34,431,8,34,10,34,12,34,
        434,9,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,444,8,35,1,
        36,1,36,1,36,1,36,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,5,38,458,
        8,38,10,38,12,38,461,9,38,1,39,1,39,1,39,1,39,1,39,1,39,5,39,469,
        8,39,10,39,12,39,472,9,39,1,40,1,40,1,40,3,40,477,8,40,1,41,1,41,
        1,41,1,41,1,41,1,41,1,41,1,41,3,41,487,8,41,1,42,1,42,1,42,5,42,
        492,8,42,10,42,12,42,495,9,42,1,43,1,43,1,43,0,4,66,68,76,78,44,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,0,
        10,1,0,14,15,1,0,33,38,1,0,47,48,1,0,51,52,1,0,49,50,1,0,53,54,1,
        0,57,62,1,0,63,64,1,0,65,67,1,0,74,76,535,0,91,1,0,0,0,2,103,1,0,
        0,0,4,105,1,0,0,0,6,122,1,0,0,0,8,130,1,0,0,0,10,134,1,0,0,0,12,
        145,1,0,0,0,14,147,1,0,0,0,16,153,1,0,0,0,18,176,1,0,0,0,20,178,
        1,0,0,0,22,186,1,0,0,0,24,188,1,0,0,0,26,194,1,0,0,0,28,199,1,0,
        0,0,30,207,1,0,0,0,32,209,1,0,0,0,34,211,1,0,0,0,36,217,1,0,0,0,
        38,219,1,0,0,0,40,225,1,0,0,0,42,247,1,0,0,0,44,249,1,0,0,0,46,280,
        1,0,0,0,48,282,1,0,0,0,50,297,1,0,0,0,52,326,1,0,0,0,54,328,1,0,
        0,0,56,336,1,0,0,0,58,354,1,0,0,0,60,388,1,0,0,0,62,390,1,0,0,0,
        64,410,1,0,0,0,66,413,1,0,0,0,68,424,1,0,0,0,70,443,1,0,0,0,72,445,
        1,0,0,0,74,449,1,0,0,0,76,451,1,0,0,0,78,462,1,0,0,0,80,473,1,0,
        0,0,82,486,1,0,0,0,84,488,1,0,0,0,86,496,1,0,0,0,88,90,3,2,1,0,89,
        88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,
        0,93,91,1,0,0,0,94,95,5,0,0,1,95,1,1,0,0,0,96,104,3,4,2,0,97,104,
        3,8,4,0,98,104,3,54,27,0,99,104,3,56,28,0,100,104,3,62,31,0,101,
        104,3,64,32,0,102,104,3,50,25,0,103,96,1,0,0,0,103,97,1,0,0,0,103,
        98,1,0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,102,
        1,0,0,0,104,3,1,0,0,0,105,106,5,1,0,0,106,107,5,77,0,0,107,109,5,
        69,0,0,108,110,3,6,3,0,109,108,1,0,0,0,109,110,1,0,0,0,110,111,1,
        0,0,0,111,115,5,70,0,0,112,114,3,2,1,0,113,112,1,0,0,0,114,117,1,
        0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,1,
        0,0,0,118,119,5,2,0,0,119,120,3,10,5,0,120,121,5,3,0,0,121,5,1,0,
        0,0,122,127,5,77,0,0,123,124,5,73,0,0,124,126,5,77,0,0,125,123,1,
        0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,7,1,0,
        0,0,129,127,1,0,0,0,130,131,5,77,0,0,131,132,5,56,0,0,132,133,3,
        10,5,0,133,9,1,0,0,0,134,139,3,12,6,0,135,136,5,55,0,0,136,138,3,
        18,9,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,
        0,0,0,140,11,1,0,0,0,141,139,1,0,0,0,142,146,3,14,7,0,143,146,3,
        16,8,0,144,146,3,76,38,0,145,142,1,0,0,0,145,143,1,0,0,0,145,144,
        1,0,0,0,146,13,1,0,0,0,147,148,5,4,0,0,148,151,5,76,0,0,149,150,
        5,5,0,0,150,152,5,76,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,15,
        1,0,0,0,153,154,5,77,0,0,154,163,5,69,0,0,155,160,3,10,5,0,156,157,
        5,73,0,0,157,159,3,10,5,0,158,156,1,0,0,0,159,162,1,0,0,0,160,158,
        1,0,0,0,160,161,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,163,155,
        1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,5,70,0,0,166,17,
        1,0,0,0,167,177,3,20,10,0,168,177,3,24,12,0,169,177,3,26,13,0,170,
        177,3,28,14,0,171,177,3,32,16,0,172,177,3,34,17,0,173,177,3,38,19,
        0,174,177,3,40,20,0,175,177,3,48,24,0,176,167,1,0,0,0,176,168,1,
        0,0,0,176,169,1,0,0,0,176,170,1,0,0,0,176,171,1,0,0,0,176,172,1,
        0,0,0,176,173,1,0,0,0,176,174,1,0,0,0,176,175,1,0,0,0,177,19,1,0,
        0,0,178,179,5,8,0,0,179,180,3,22,11,0,180,21,1,0,0,0,181,182,5,71,
        0,0,182,183,3,84,42,0,183,184,5,72,0,0,184,187,1,0,0,0,185,187,3,
        84,42,0,186,181,1,0,0,0,186,185,1,0,0,0,187,23,1,0,0,0,188,190,5,
        9,0,0,189,191,5,10,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,
        0,0,0,192,193,3,66,33,0,193,25,1,0,0,0,194,195,5,11,0,0,195,196,
        5,77,0,0,196,197,5,56,0,0,197,198,3,76,38,0,198,27,1,0,0,0,199,201,
        5,12,0,0,200,202,5,13,0,0,201,200,1,0,0,0,201,202,1,0,0,0,202,203,
        1,0,0,0,203,205,5,77,0,0,204,206,3,30,15,0,205,204,1,0,0,0,205,206,
        1,0,0,0,206,29,1,0,0,0,207,208,7,0,0,0,208,31,1,0,0,0,209,210,5,
        16,0,0,210,33,1,0,0,0,211,212,5,17,0,0,212,213,3,36,18,0,213,35,
        1,0,0,0,214,218,5,18,0,0,215,216,5,19,0,0,216,218,3,86,43,0,217,
        214,1,0,0,0,217,215,1,0,0,0,218,37,1,0,0,0,219,221,5,20,0,0,220,
        222,5,13,0,0,221,220,1,0,0,0,221,222,1,0,0,0,222,223,1,0,0,0,223,
        224,3,22,11,0,224,39,1,0,0,0,225,226,5,21,0,0,226,227,3,42,21,0,
        227,41,1,0,0,0,228,229,5,71,0,0,229,234,3,44,22,0,230,231,5,73,0,
        0,231,233,3,44,22,0,232,230,1,0,0,0,233,236,1,0,0,0,234,232,1,0,
        0,0,234,235,1,0,0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,238,5,72,
        0,0,238,248,1,0,0,0,239,244,3,44,22,0,240,241,5,73,0,0,241,243,3,
        44,22,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,247,228,1,0,0,0,247,239,
        1,0,0,0,248,43,1,0,0,0,249,250,5,77,0,0,250,251,5,56,0,0,251,252,
        3,46,23,0,252,45,1,0,0,0,253,254,5,24,0,0,254,255,5,69,0,0,255,281,
        5,70,0,0,256,257,5,25,0,0,257,258,5,69,0,0,258,259,5,77,0,0,259,
        281,5,70,0,0,260,261,5,26,0,0,261,262,5,69,0,0,262,263,5,77,0,0,
        263,281,5,70,0,0,264,265,5,27,0,0,265,266,5,69,0,0,266,267,5,77,
        0,0,267,281,5,70,0,0,268,269,5,28,0,0,269,270,5,69,0,0,270,271,5,
        77,0,0,271,281,5,70,0,0,272,273,5,29,0,0,273,274,5,69,0,0,274,275,
        5,77,0,0,275,281,5,70,0,0,276,277,5,30,0,0,277,278,5,69,0,0,278,
        279,5,77,0,0,279,281,5,70,0,0,280,253,1,0,0,0,280,256,1,0,0,0,280,
        260,1,0,0,0,280,264,1,0,0,0,280,268,1,0,0,0,280,272,1,0,0,0,280,
        276,1,0,0,0,281,47,1,0,0,0,282,284,5,22,0,0,283,285,5,71,0,0,284,
        283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,291,3,52,26,0,287,
        288,5,73,0,0,288,290,3,52,26,0,289,287,1,0,0,0,290,293,1,0,0,0,291,
        289,1,0,0,0,291,292,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,294,
        296,5,72,0,0,295,294,1,0,0,0,295,296,1,0,0,0,296,49,1,0,0,0,297,
        298,5,22,0,0,298,300,5,77,0,0,299,301,5,71,0,0,300,299,1,0,0,0,300,
        301,1,0,0,0,301,302,1,0,0,0,302,307,3,52,26,0,303,304,5,73,0,0,304,
        306,3,52,26,0,305,303,1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,307,
        308,1,0,0,0,308,311,1,0,0,0,309,307,1,0,0,0,310,312,5,72,0,0,311,
        310,1,0,0,0,311,312,1,0,0,0,312,51,1,0,0,0,313,314,5,39,0,0,314,
        315,5,56,0,0,315,327,5,77,0,0,316,317,5,40,0,0,317,318,5,56,0,0,
        318,327,5,77,0,0,319,320,5,23,0,0,320,321,5,56,0,0,321,327,5,77,
        0,0,322,323,5,77,0,0,323,324,5,56,0,0,324,327,5,77,0,0,325,327,5,
        77,0,0,326,313,1,0,0,0,326,316,1,0,0,0,326,319,1,0,0,0,326,322,1,
        0,0,0,326,325,1,0,0,0,327,53,1,0,0,0,328,329,5,6,0,0,329,330,5,77,
        0,0,330,331,5,7,0,0,331,334,5,76,0,0,332,333,5,5,0,0,333,335,5,76,
        0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,55,1,0,0,0,336,337,5,31,
        0,0,337,338,3,58,29,0,338,340,5,77,0,0,339,341,5,71,0,0,340,339,
        1,0,0,0,340,341,1,0,0,0,341,345,1,0,0,0,342,344,3,60,30,0,343,342,
        1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,345,346,1,0,0,0,346,349,
        1,0,0,0,347,345,1,0,0,0,348,350,5,72,0,0,349,348,1,0,0,0,349,350,
        1,0,0,0,350,352,1,0,0,0,351,353,5,32,0,0,352,351,1,0,0,0,352,353,
        1,0,0,0,353,57,1,0,0,0,354,355,7,1,0,0,355,59,1,0,0,0,356,358,5,
        39,0,0,357,359,5,56,0,0,358,357,1,0,0,0,358,359,1,0,0,0,359,360,
        1,0,0,0,360,362,5,76,0,0,361,363,5,73,0,0,362,361,1,0,0,0,362,363,
        1,0,0,0,363,389,1,0,0,0,364,366,5,40,0,0,365,367,5,56,0,0,366,365,
        1,0,0,0,366,367,1,0,0,0,367,368,1,0,0,0,368,370,5,76,0,0,369,371,
        5,73,0,0,370,369,1,0,0,0,370,371,1,0,0,0,371,389,1,0,0,0,372,374,
        5,41,0,0,373,375,5,56,0,0,374,373,1,0,0,0,374,375,1,0,0,0,375,376,
        1,0,0,0,376,378,5,76,0,0,377,379,5,73,0,0,378,377,1,0,0,0,378,379,
        1,0,0,0,379,389,1,0,0,0,380,382,5,42,0,0,381,383,5,56,0,0,382,381,
        1,0,0,0,382,383,1,0,0,0,383,384,1,0,0,0,384,386,5,76,0,0,385,387,
        5,73,0,0,386,385,1,0,0,0,386,387,1,0,0,0,387,389,1,0,0,0,388,356,
        1,0,0,0,388,364,1,0,0,0,388,372,1,0,0,0,388,380,1,0,0,0,389,61,1,
        0,0,0,390,391,5,43,0,0,391,392,3,66,33,0,392,396,5,44,0,0,393,395,
        3,2,1,0,394,393,1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,
        1,0,0,0,397,406,1,0,0,0,398,396,1,0,0,0,399,403,5,45,0,0,400,402,
        3,2,1,0,401,400,1,0,0,0,402,405,1,0,0,0,403,401,1,0,0,0,403,404,
        1,0,0,0,404,407,1,0,0,0,405,403,1,0,0,0,406,399,1,0,0,0,406,407,
        1,0,0,0,407,408,1,0,0,0,408,409,5,46,0,0,409,63,1,0,0,0,410,411,
        7,2,0,0,411,412,3,10,5,0,412,65,1,0,0,0,413,414,6,33,-1,0,414,415,
        3,68,34,0,415,421,1,0,0,0,416,417,10,2,0,0,417,418,7,3,0,0,418,420,
        3,68,34,0,419,416,1,0,0,0,420,423,1,0,0,0,421,419,1,0,0,0,421,422,
        1,0,0,0,422,67,1,0,0,0,423,421,1,0,0,0,424,425,6,34,-1,0,425,426,
        3,70,35,0,426,432,1,0,0,0,427,428,10,2,0,0,428,429,7,4,0,0,429,431,
        3,70,35,0,430,427,1,0,0,0,431,434,1,0,0,0,432,430,1,0,0,0,432,433,
        1,0,0,0,433,69,1,0,0,0,434,432,1,0,0,0,435,436,7,5,0,0,436,444,3,
        70,35,0,437,444,3,72,36,0,438,439,5,69,0,0,439,440,3,66,33,0,440,
        441,5,70,0,0,441,444,1,0,0,0,442,444,5,74,0,0,443,435,1,0,0,0,443,
        437,1,0,0,0,443,438,1,0,0,0,443,442,1,0,0,0,444,71,1,0,0,0,445,446,
        3,76,38,0,446,447,3,74,37,0,447,448,3,76,38,0,448,73,1,0,0,0,449,
        450,7,6,0,0,450,75,1,0,0,0,451,452,6,38,-1,0,452,453,3,78,39,0,453,
        459,1,0,0,0,454,455,10,2,0,0,455,456,7,7,0,0,456,458,3,78,39,0,457,
        454,1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,460,
        77,1,0,0,0,461,459,1,0,0,0,462,463,6,39,-1,0,463,464,3,80,40,0,464,
        470,1,0,0,0,465,466,10,2,0,0,466,467,7,8,0,0,467,469,3,80,40,0,468,
        465,1,0,0,0,469,472,1,0,0,0,470,468,1,0,0,0,470,471,1,0,0,0,471,
        79,1,0,0,0,472,470,1,0,0,0,473,476,3,82,41,0,474,475,5,68,0,0,475,
        477,3,80,40,0,476,474,1,0,0,0,476,477,1,0,0,0,477,81,1,0,0,0,478,
        487,5,75,0,0,479,487,5,76,0,0,480,487,5,74,0,0,481,487,5,77,0,0,
        482,483,5,69,0,0,483,484,3,76,38,0,484,485,5,70,0,0,485,487,1,0,
        0,0,486,478,1,0,0,0,486,479,1,0,0,0,486,480,1,0,0,0,486,481,1,0,
        0,0,486,482,1,0,0,0,487,83,1,0,0,0,488,493,5,77,0,0,489,490,5,73,
        0,0,490,492,5,77,0,0,491,489,1,0,0,0,492,495,1,0,0,0,493,491,1,0,
        0,0,493,494,1,0,0,0,494,85,1,0,0,0,495,493,1,0,0,0,496,497,7,9,0,
        0,497,87,1,0,0,0,53,91,103,109,115,127,139,145,151,160,163,176,186,
        190,201,205,217,221,234,244,247,280,284,291,295,300,307,311,326,
        334,340,345,349,352,358,362,366,370,374,378,382,386,388,396,403,
        406,421,432,443,459,470,476,486,493
    ]

# Compatibilidad retroactiva con antlr4 runtime < 4.11 (p. ej. en Debian / Kali Linux)
try:
    if hasattr(ATNDeserializer, "reset"):
        _orig_atn_reset = ATNDeserializer.reset
        def _compat_atn_reset(self, data):
            if data and isinstance(data[0], int):
                self.data = list(data)
                self.pos = 0
            else:
                _orig_atn_reset(self, data)
        ATNDeserializer.reset = _compat_atn_reset
except Exception:
    pass

class HolocronDSLParser ( Parser ):

    grammarFileName = "HolocronDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'mision'", "<INVALID>", "'fin_mision'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'en'", "<INVALID>", 
                     "<INVALID>", "'donde'", "<INVALID>", "<INVALID>", "'por'", 
                     "<INVALID>", "<INVALID>", "'eliminar_clones'", "'sanar_vacios'", 
                     "'descartar'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'mediana'", "<INVALID>", "<INVALID>", 
                     "'desviacion'", "<INVALID>", "'fin_holograma'", "'barras'", 
                     "'lineas'", "'dispersion'", "'histograma'", "<INVALID>", 
                     "<INVALID>", "'eje_x'", "'eje_y'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'mostrar'", "'y'", "'y_fuerza'", "'o'", 
                     "'o_fuerza'", "'no'", "'no_fuerza'", "<INVALID>", "'='", 
                     "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'^'", "'('", "')'", "'['", 
                     "']'", "','" ]

    symbolicNames = [ "<INVALID>", "MISION", "RETORNAR", "FIN_MISION", "ABRIR_HOLOCRON", 
                      "DELIMITADO_POR", "ARCHIVAR_HOLOCRON", "EN", "REVELAR", 
                      "PURGAR", "DONDE", "FORJAR", "ORDENAR", "POR", "ASCENDENTE", 
                      "DESCENDENTE", "ELIMINAR_CLONES", "SANAR_VACIOS", 
                      "DESCARTAR", "CON", "AGRUPAR", "RESUMIR", "TRAZAR_REGRESION", 
                      "DESTINO", "FUNC_RECUENTO", "FUNC_ACUMULAR", "FUNC_EQUILIBRIO", 
                      "FUNC_MEDIANA", "FUNC_CENIT", "FUNC_NADIR", "FUNC_DESVIACION", 
                      "HOLOGRAMA", "FIN_HOLOGRAMA", "TIPO_BARRAS", "TIPO_LINEAS", 
                      "TIPO_DISPERSION", "TIPO_HISTOGRAMA", "TIPO_CAJA", 
                      "TIPO_REGRESION", "EJE_X", "EJE_Y", "TITULO", "GUARDAR", 
                      "EVALUAR_FUERZA", "SENDA_LUMINOSA", "SENDA_OSCURA", 
                      "FIN_EVALUAR", "TRANSMITIR", "MOSTRAR", "Y_LOGICO", 
                      "Y_FUERZA", "O_LOGICO", "O_FUERZA", "NO_LOGICO", "NO_FUERZA", 
                      "PIPE", "OP_ASIG", "OP_IGUAL", "OP_DIFERENTE", "OP_MENOR_IGUAL", 
                      "OP_MAYOR_IGUAL", "OP_MENOR", "OP_MAYOR", "OP_SUMA", 
                      "OP_RESTA", "OP_MULT", "OP_DIV", "OP_MOD", "OP_POTENCIA", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "BOOL", 
                      "NUMERO", "CADENA", "ID", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE", 
                      "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_declaracionMision = 2
    RULE_listaParametros = 3
    RULE_sentenciaAsignacion = 4
    RULE_expresionPipeline = 5
    RULE_expresionBase = 6
    RULE_instruccionCarga = 7
    RULE_llamadaMision = 8
    RULE_operacionPipeline = 9
    RULE_operacionSeleccionar = 10
    RULE_listaIdentificadoresOpcional = 11
    RULE_operacionFiltrar = 12
    RULE_operacionForjar = 13
    RULE_operacionOrdenar = 14
    RULE_ordenDireccion = 15
    RULE_operacionEliminarClones = 16
    RULE_operacionSanarVacios = 17
    RULE_opcionSanado = 18
    RULE_operacionAgrupar = 19
    RULE_operacionResumir = 20
    RULE_listaAsignacionesAgregacion = 21
    RULE_asignacionAgregacion = 22
    RULE_llamadaAgregacion = 23
    RULE_operacionRegresion = 24
    RULE_sentenciaRegresion = 25
    RULE_parametroRegresion = 26
    RULE_sentenciaArchivado = 27
    RULE_sentenciaHolograma = 28
    RULE_tipoGrafica = 29
    RULE_propiedadHolograma = 30
    RULE_sentenciaCondicional = 31
    RULE_sentenciaTransmision = 32
    RULE_expresionBooleana = 33
    RULE_terminoBooleano = 34
    RULE_factorBooleano = 35
    RULE_comparacionRelacional = 36
    RULE_operadorRelacional = 37
    RULE_expresionAritmetica = 38
    RULE_terminoAritmetico = 39
    RULE_factorPotencia = 40
    RULE_atomoAritmetico = 41
    RULE_listaIdentificadores = 42
    RULE_literal = 43

    ruleNames =  [ "programa", "sentencia", "declaracionMision", "listaParametros", 
                   "sentenciaAsignacion", "expresionPipeline", "expresionBase", 
                   "instruccionCarga", "llamadaMision", "operacionPipeline", 
                   "operacionSeleccionar", "listaIdentificadoresOpcional", 
                   "operacionFiltrar", "operacionForjar", "operacionOrdenar", 
                   "ordenDireccion", "operacionEliminarClones", "operacionSanarVacios", 
                   "opcionSanado", "operacionAgrupar", "operacionResumir", 
                   "listaAsignacionesAgregacion", "asignacionAgregacion", 
                   "llamadaAgregacion", "operacionRegresion", "sentenciaRegresion", 
                   "parametroRegresion", "sentenciaArchivado", "sentenciaHolograma", 
                   "tipoGrafica", "propiedadHolograma", "sentenciaCondicional", 
                   "sentenciaTransmision", "expresionBooleana", "terminoBooleano", 
                   "factorBooleano", "comparacionRelacional", "operadorRelacional", 
                   "expresionAritmetica", "terminoAritmetico", "factorPotencia", 
                   "atomoAritmetico", "listaIdentificadores", "literal" ]

    EOF = Token.EOF
    MISION=1
    RETORNAR=2
    FIN_MISION=3
    ABRIR_HOLOCRON=4
    DELIMITADO_POR=5
    ARCHIVAR_HOLOCRON=6
    EN=7
    REVELAR=8
    PURGAR=9
    DONDE=10
    FORJAR=11
    ORDENAR=12
    POR=13
    ASCENDENTE=14
    DESCENDENTE=15
    ELIMINAR_CLONES=16
    SANAR_VACIOS=17
    DESCARTAR=18
    CON=19
    AGRUPAR=20
    RESUMIR=21
    TRAZAR_REGRESION=22
    DESTINO=23
    FUNC_RECUENTO=24
    FUNC_ACUMULAR=25
    FUNC_EQUILIBRIO=26
    FUNC_MEDIANA=27
    FUNC_CENIT=28
    FUNC_NADIR=29
    FUNC_DESVIACION=30
    HOLOGRAMA=31
    FIN_HOLOGRAMA=32
    TIPO_BARRAS=33
    TIPO_LINEAS=34
    TIPO_DISPERSION=35
    TIPO_HISTOGRAMA=36
    TIPO_CAJA=37
    TIPO_REGRESION=38
    EJE_X=39
    EJE_Y=40
    TITULO=41
    GUARDAR=42
    EVALUAR_FUERZA=43
    SENDA_LUMINOSA=44
    SENDA_OSCURA=45
    FIN_EVALUAR=46
    TRANSMITIR=47
    MOSTRAR=48
    Y_LOGICO=49
    Y_FUERZA=50
    O_LOGICO=51
    O_FUERZA=52
    NO_LOGICO=53
    NO_FUERZA=54
    PIPE=55
    OP_ASIG=56
    OP_IGUAL=57
    OP_DIFERENTE=58
    OP_MENOR_IGUAL=59
    OP_MAYOR_IGUAL=60
    OP_MENOR=61
    OP_MAYOR=62
    OP_SUMA=63
    OP_RESTA=64
    OP_MULT=65
    OP_DIV=66
    OP_MOD=67
    OP_POTENCIA=68
    LPAREN=69
    RPAREN=70
    LBRACK=71
    RBRACK=72
    COMMA=73
    BOOL=74
    NUMERO=75
    CADENA=76
    ID=77
    COMENTARIO_LINEA=78
    COMENTARIO_BLOQUE=79
    WS=80

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HolocronDSLParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.SentenciaContext,i)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = HolocronDSLParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 431010709766210) != 0) or _la==77:
                self.state = 88
                self.sentencia()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(HolocronDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionMision(self):
            return self.getTypedRuleContext(HolocronDSLParser.DeclaracionMisionContext,0)


        def sentenciaAsignacion(self):
            return self.getTypedRuleContext(HolocronDSLParser.SentenciaAsignacionContext,0)


        def sentenciaArchivado(self):
            return self.getTypedRuleContext(HolocronDSLParser.SentenciaArchivadoContext,0)


        def sentenciaHolograma(self):
            return self.getTypedRuleContext(HolocronDSLParser.SentenciaHologramaContext,0)


        def sentenciaCondicional(self):
            return self.getTypedRuleContext(HolocronDSLParser.SentenciaCondicionalContext,0)


        def sentenciaTransmision(self):
            return self.getTypedRuleContext(HolocronDSLParser.SentenciaTransmisionContext,0)


        def sentenciaRegresion(self):
            return self.getTypedRuleContext(HolocronDSLParser.SentenciaRegresionContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = HolocronDSLParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.declaracionMision()
                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.sentenciaAsignacion()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.sentenciaArchivado()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.sentenciaHolograma()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.sentenciaCondicional()
                pass
            elif token in [47, 48]:
                self.enterOuterAlt(localctx, 6)
                self.state = 101
                self.sentenciaTransmision()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 7)
                self.state = 102
                self.sentenciaRegresion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionMisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MISION(self):
            return self.getToken(HolocronDSLParser.MISION, 0)

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(HolocronDSLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(HolocronDSLParser.RPAREN, 0)

        def RETORNAR(self):
            return self.getToken(HolocronDSLParser.RETORNAR, 0)

        def expresionPipeline(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionPipelineContext,0)


        def FIN_MISION(self):
            return self.getToken(HolocronDSLParser.FIN_MISION, 0)

        def listaParametros(self):
            return self.getTypedRuleContext(HolocronDSLParser.ListaParametrosContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.SentenciaContext,i)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_declaracionMision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionMision" ):
                listener.enterDeclaracionMision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionMision" ):
                listener.exitDeclaracionMision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionMision" ):
                return visitor.visitDeclaracionMision(self)
            else:
                return visitor.visitChildren(self)




    def declaracionMision(self):

        localctx = HolocronDSLParser.DeclaracionMisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracionMision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(HolocronDSLParser.MISION)
            self.state = 106
            self.match(HolocronDSLParser.ID)
            self.state = 107
            self.match(HolocronDSLParser.LPAREN)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==77:
                self.state = 108
                self.listaParametros()


            self.state = 111
            self.match(HolocronDSLParser.RPAREN)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 431010709766210) != 0) or _la==77:
                self.state = 112
                self.sentencia()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(HolocronDSLParser.RETORNAR)
            self.state = 119
            self.expresionPipeline()
            self.state = 120
            self.match(HolocronDSLParser.FIN_MISION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.ID)
            else:
                return self.getToken(HolocronDSLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.COMMA)
            else:
                return self.getToken(HolocronDSLParser.COMMA, i)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_listaParametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParametros" ):
                listener.enterListaParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParametros" ):
                listener.exitListaParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParametros" ):
                return visitor.visitListaParametros(self)
            else:
                return visitor.visitChildren(self)




    def listaParametros(self):

        localctx = HolocronDSLParser.ListaParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listaParametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(HolocronDSLParser.ID)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==73:
                self.state = 123
                self.match(HolocronDSLParser.COMMA)
                self.state = 124
                self.match(HolocronDSLParser.ID)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaAsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def OP_ASIG(self):
            return self.getToken(HolocronDSLParser.OP_ASIG, 0)

        def expresionPipeline(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionPipelineContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_sentenciaAsignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaAsignacion" ):
                listener.enterSentenciaAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaAsignacion" ):
                listener.exitSentenciaAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaAsignacion" ):
                return visitor.visitSentenciaAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaAsignacion(self):

        localctx = HolocronDSLParser.SentenciaAsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sentenciaAsignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(HolocronDSLParser.ID)
            self.state = 131
            self.match(HolocronDSLParser.OP_ASIG)
            self.state = 132
            self.expresionPipeline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionPipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionBase(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionBaseContext,0)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.PIPE)
            else:
                return self.getToken(HolocronDSLParser.PIPE, i)

        def operacionPipeline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.OperacionPipelineContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.OperacionPipelineContext,i)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_expresionPipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionPipeline" ):
                listener.enterExpresionPipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionPipeline" ):
                listener.exitExpresionPipeline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionPipeline" ):
                return visitor.visitExpresionPipeline(self)
            else:
                return visitor.visitChildren(self)




    def expresionPipeline(self):

        localctx = HolocronDSLParser.ExpresionPipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expresionPipeline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.expresionBase()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 135
                self.match(HolocronDSLParser.PIPE)
                self.state = 136
                self.operacionPipeline()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionBaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccionCarga(self):
            return self.getTypedRuleContext(HolocronDSLParser.InstruccionCargaContext,0)


        def llamadaMision(self):
            return self.getTypedRuleContext(HolocronDSLParser.LlamadaMisionContext,0)


        def expresionAritmetica(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionAritmeticaContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_expresionBase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionBase" ):
                listener.enterExpresionBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionBase" ):
                listener.exitExpresionBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionBase" ):
                return visitor.visitExpresionBase(self)
            else:
                return visitor.visitChildren(self)




    def expresionBase(self):

        localctx = HolocronDSLParser.ExpresionBaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expresionBase)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.instruccionCarga()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.llamadaMision()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.expresionAritmetica(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionCargaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRIR_HOLOCRON(self):
            return self.getToken(HolocronDSLParser.ABRIR_HOLOCRON, 0)

        def CADENA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.CADENA)
            else:
                return self.getToken(HolocronDSLParser.CADENA, i)

        def DELIMITADO_POR(self):
            return self.getToken(HolocronDSLParser.DELIMITADO_POR, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_instruccionCarga

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionCarga" ):
                listener.enterInstruccionCarga(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionCarga" ):
                listener.exitInstruccionCarga(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionCarga" ):
                return visitor.visitInstruccionCarga(self)
            else:
                return visitor.visitChildren(self)




    def instruccionCarga(self):

        localctx = HolocronDSLParser.InstruccionCargaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instruccionCarga)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(HolocronDSLParser.ABRIR_HOLOCRON)
            self.state = 148
            self.match(HolocronDSLParser.CADENA)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 149
                self.match(HolocronDSLParser.DELIMITADO_POR)
                self.state = 150
                self.match(HolocronDSLParser.CADENA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaMisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(HolocronDSLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(HolocronDSLParser.RPAREN, 0)

        def expresionPipeline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.ExpresionPipelineContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.ExpresionPipelineContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.COMMA)
            else:
                return self.getToken(HolocronDSLParser.COMMA, i)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_llamadaMision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaMision" ):
                listener.enterLlamadaMision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaMision" ):
                listener.exitLlamadaMision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaMision" ):
                return visitor.visitLlamadaMision(self)
            else:
                return visitor.visitChildren(self)




    def llamadaMision(self):

        localctx = HolocronDSLParser.LlamadaMisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_llamadaMision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(HolocronDSLParser.ID)
            self.state = 154
            self.match(HolocronDSLParser.LPAREN)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 481) != 0):
                self.state = 155
                self.expresionPipeline()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==73:
                    self.state = 156
                    self.match(HolocronDSLParser.COMMA)
                    self.state = 157
                    self.expresionPipeline()
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 165
            self.match(HolocronDSLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionPipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacionSeleccionar(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionSeleccionarContext,0)


        def operacionFiltrar(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionFiltrarContext,0)


        def operacionForjar(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionForjarContext,0)


        def operacionOrdenar(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionOrdenarContext,0)


        def operacionEliminarClones(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionEliminarClonesContext,0)


        def operacionSanarVacios(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionSanarVaciosContext,0)


        def operacionAgrupar(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionAgruparContext,0)


        def operacionResumir(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionResumirContext,0)


        def operacionRegresion(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperacionRegresionContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionPipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionPipeline" ):
                listener.enterOperacionPipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionPipeline" ):
                listener.exitOperacionPipeline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionPipeline" ):
                return visitor.visitOperacionPipeline(self)
            else:
                return visitor.visitChildren(self)




    def operacionPipeline(self):

        localctx = HolocronDSLParser.OperacionPipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operacionPipeline)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.operacionSeleccionar()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.operacionFiltrar()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.operacionForjar()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.operacionOrdenar()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 171
                self.operacionEliminarClones()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 172
                self.operacionSanarVacios()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 173
                self.operacionAgrupar()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 8)
                self.state = 174
                self.operacionResumir()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 9)
                self.state = 175
                self.operacionRegresion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionSeleccionarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REVELAR(self):
            return self.getToken(HolocronDSLParser.REVELAR, 0)

        def listaIdentificadoresOpcional(self):
            return self.getTypedRuleContext(HolocronDSLParser.ListaIdentificadoresOpcionalContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionSeleccionar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionSeleccionar" ):
                listener.enterOperacionSeleccionar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionSeleccionar" ):
                listener.exitOperacionSeleccionar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionSeleccionar" ):
                return visitor.visitOperacionSeleccionar(self)
            else:
                return visitor.visitChildren(self)




    def operacionSeleccionar(self):

        localctx = HolocronDSLParser.OperacionSeleccionarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operacionSeleccionar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(HolocronDSLParser.REVELAR)
            self.state = 179
            self.listaIdentificadoresOpcional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdentificadoresOpcionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(HolocronDSLParser.LBRACK, 0)

        def listaIdentificadores(self):
            return self.getTypedRuleContext(HolocronDSLParser.ListaIdentificadoresContext,0)


        def RBRACK(self):
            return self.getToken(HolocronDSLParser.RBRACK, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_listaIdentificadoresOpcional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIdentificadoresOpcional" ):
                listener.enterListaIdentificadoresOpcional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIdentificadoresOpcional" ):
                listener.exitListaIdentificadoresOpcional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaIdentificadoresOpcional" ):
                return visitor.visitListaIdentificadoresOpcional(self)
            else:
                return visitor.visitChildren(self)




    def listaIdentificadoresOpcional(self):

        localctx = HolocronDSLParser.ListaIdentificadoresOpcionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listaIdentificadoresOpcional)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [71]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(HolocronDSLParser.LBRACK)
                self.state = 182
                self.listaIdentificadores()
                self.state = 183
                self.match(HolocronDSLParser.RBRACK)
                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.listaIdentificadores()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionFiltrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PURGAR(self):
            return self.getToken(HolocronDSLParser.PURGAR, 0)

        def expresionBooleana(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionBooleanaContext,0)


        def DONDE(self):
            return self.getToken(HolocronDSLParser.DONDE, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionFiltrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionFiltrar" ):
                listener.enterOperacionFiltrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionFiltrar" ):
                listener.exitOperacionFiltrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionFiltrar" ):
                return visitor.visitOperacionFiltrar(self)
            else:
                return visitor.visitChildren(self)




    def operacionFiltrar(self):

        localctx = HolocronDSLParser.OperacionFiltrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operacionFiltrar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(HolocronDSLParser.PURGAR)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 189
                self.match(HolocronDSLParser.DONDE)


            self.state = 192
            self.expresionBooleana(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionForjarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORJAR(self):
            return self.getToken(HolocronDSLParser.FORJAR, 0)

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def OP_ASIG(self):
            return self.getToken(HolocronDSLParser.OP_ASIG, 0)

        def expresionAritmetica(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionAritmeticaContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionForjar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionForjar" ):
                listener.enterOperacionForjar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionForjar" ):
                listener.exitOperacionForjar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionForjar" ):
                return visitor.visitOperacionForjar(self)
            else:
                return visitor.visitChildren(self)




    def operacionForjar(self):

        localctx = HolocronDSLParser.OperacionForjarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operacionForjar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(HolocronDSLParser.FORJAR)
            self.state = 195
            self.match(HolocronDSLParser.ID)
            self.state = 196
            self.match(HolocronDSLParser.OP_ASIG)
            self.state = 197
            self.expresionAritmetica(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionOrdenarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDENAR(self):
            return self.getToken(HolocronDSLParser.ORDENAR, 0)

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def POR(self):
            return self.getToken(HolocronDSLParser.POR, 0)

        def ordenDireccion(self):
            return self.getTypedRuleContext(HolocronDSLParser.OrdenDireccionContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionOrdenar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionOrdenar" ):
                listener.enterOperacionOrdenar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionOrdenar" ):
                listener.exitOperacionOrdenar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionOrdenar" ):
                return visitor.visitOperacionOrdenar(self)
            else:
                return visitor.visitChildren(self)




    def operacionOrdenar(self):

        localctx = HolocronDSLParser.OperacionOrdenarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_operacionOrdenar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(HolocronDSLParser.ORDENAR)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 200
                self.match(HolocronDSLParser.POR)


            self.state = 203
            self.match(HolocronDSLParser.ID)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14 or _la==15:
                self.state = 204
                self.ordenDireccion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrdenDireccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASCENDENTE(self):
            return self.getToken(HolocronDSLParser.ASCENDENTE, 0)

        def DESCENDENTE(self):
            return self.getToken(HolocronDSLParser.DESCENDENTE, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_ordenDireccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrdenDireccion" ):
                listener.enterOrdenDireccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrdenDireccion" ):
                listener.exitOrdenDireccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrdenDireccion" ):
                return visitor.visitOrdenDireccion(self)
            else:
                return visitor.visitChildren(self)




    def ordenDireccion(self):

        localctx = HolocronDSLParser.OrdenDireccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ordenDireccion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionEliminarClonesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIMINAR_CLONES(self):
            return self.getToken(HolocronDSLParser.ELIMINAR_CLONES, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionEliminarClones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionEliminarClones" ):
                listener.enterOperacionEliminarClones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionEliminarClones" ):
                listener.exitOperacionEliminarClones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionEliminarClones" ):
                return visitor.visitOperacionEliminarClones(self)
            else:
                return visitor.visitChildren(self)




    def operacionEliminarClones(self):

        localctx = HolocronDSLParser.OperacionEliminarClonesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_operacionEliminarClones)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(HolocronDSLParser.ELIMINAR_CLONES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionSanarVaciosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SANAR_VACIOS(self):
            return self.getToken(HolocronDSLParser.SANAR_VACIOS, 0)

        def opcionSanado(self):
            return self.getTypedRuleContext(HolocronDSLParser.OpcionSanadoContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionSanarVacios

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionSanarVacios" ):
                listener.enterOperacionSanarVacios(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionSanarVacios" ):
                listener.exitOperacionSanarVacios(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionSanarVacios" ):
                return visitor.visitOperacionSanarVacios(self)
            else:
                return visitor.visitChildren(self)




    def operacionSanarVacios(self):

        localctx = HolocronDSLParser.OperacionSanarVaciosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_operacionSanarVacios)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(HolocronDSLParser.SANAR_VACIOS)
            self.state = 212
            self.opcionSanado()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcionSanadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCARTAR(self):
            return self.getToken(HolocronDSLParser.DESCARTAR, 0)

        def CON(self):
            return self.getToken(HolocronDSLParser.CON, 0)

        def literal(self):
            return self.getTypedRuleContext(HolocronDSLParser.LiteralContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_opcionSanado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcionSanado" ):
                listener.enterOpcionSanado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcionSanado" ):
                listener.exitOpcionSanado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcionSanado" ):
                return visitor.visitOpcionSanado(self)
            else:
                return visitor.visitChildren(self)




    def opcionSanado(self):

        localctx = HolocronDSLParser.OpcionSanadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_opcionSanado)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(HolocronDSLParser.DESCARTAR)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(HolocronDSLParser.CON)
                self.state = 216
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionAgruparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGRUPAR(self):
            return self.getToken(HolocronDSLParser.AGRUPAR, 0)

        def listaIdentificadoresOpcional(self):
            return self.getTypedRuleContext(HolocronDSLParser.ListaIdentificadoresOpcionalContext,0)


        def POR(self):
            return self.getToken(HolocronDSLParser.POR, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionAgrupar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionAgrupar" ):
                listener.enterOperacionAgrupar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionAgrupar" ):
                listener.exitOperacionAgrupar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionAgrupar" ):
                return visitor.visitOperacionAgrupar(self)
            else:
                return visitor.visitChildren(self)




    def operacionAgrupar(self):

        localctx = HolocronDSLParser.OperacionAgruparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operacionAgrupar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(HolocronDSLParser.AGRUPAR)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 220
                self.match(HolocronDSLParser.POR)


            self.state = 223
            self.listaIdentificadoresOpcional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionResumirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RESUMIR(self):
            return self.getToken(HolocronDSLParser.RESUMIR, 0)

        def listaAsignacionesAgregacion(self):
            return self.getTypedRuleContext(HolocronDSLParser.ListaAsignacionesAgregacionContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionResumir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionResumir" ):
                listener.enterOperacionResumir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionResumir" ):
                listener.exitOperacionResumir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionResumir" ):
                return visitor.visitOperacionResumir(self)
            else:
                return visitor.visitChildren(self)




    def operacionResumir(self):

        localctx = HolocronDSLParser.OperacionResumirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operacionResumir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(HolocronDSLParser.RESUMIR)
            self.state = 226
            self.listaAsignacionesAgregacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAsignacionesAgregacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(HolocronDSLParser.LBRACK, 0)

        def asignacionAgregacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.AsignacionAgregacionContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.AsignacionAgregacionContext,i)


        def RBRACK(self):
            return self.getToken(HolocronDSLParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.COMMA)
            else:
                return self.getToken(HolocronDSLParser.COMMA, i)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_listaAsignacionesAgregacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAsignacionesAgregacion" ):
                listener.enterListaAsignacionesAgregacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAsignacionesAgregacion" ):
                listener.exitListaAsignacionesAgregacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAsignacionesAgregacion" ):
                return visitor.visitListaAsignacionesAgregacion(self)
            else:
                return visitor.visitChildren(self)




    def listaAsignacionesAgregacion(self):

        localctx = HolocronDSLParser.ListaAsignacionesAgregacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_listaAsignacionesAgregacion)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [71]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(HolocronDSLParser.LBRACK)
                self.state = 229
                self.asignacionAgregacion()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==73:
                    self.state = 230
                    self.match(HolocronDSLParser.COMMA)
                    self.state = 231
                    self.asignacionAgregacion()
                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 237
                self.match(HolocronDSLParser.RBRACK)
                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.asignacionAgregacion()
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 240
                        self.match(HolocronDSLParser.COMMA)
                        self.state = 241
                        self.asignacionAgregacion() 
                    self.state = 246
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionAgregacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def OP_ASIG(self):
            return self.getToken(HolocronDSLParser.OP_ASIG, 0)

        def llamadaAgregacion(self):
            return self.getTypedRuleContext(HolocronDSLParser.LlamadaAgregacionContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_asignacionAgregacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionAgregacion" ):
                listener.enterAsignacionAgregacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionAgregacion" ):
                listener.exitAsignacionAgregacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionAgregacion" ):
                return visitor.visitAsignacionAgregacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacionAgregacion(self):

        localctx = HolocronDSLParser.AsignacionAgregacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_asignacionAgregacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(HolocronDSLParser.ID)
            self.state = 250
            self.match(HolocronDSLParser.OP_ASIG)
            self.state = 251
            self.llamadaAgregacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaAgregacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_RECUENTO(self):
            return self.getToken(HolocronDSLParser.FUNC_RECUENTO, 0)

        def LPAREN(self):
            return self.getToken(HolocronDSLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(HolocronDSLParser.RPAREN, 0)

        def FUNC_ACUMULAR(self):
            return self.getToken(HolocronDSLParser.FUNC_ACUMULAR, 0)

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def FUNC_EQUILIBRIO(self):
            return self.getToken(HolocronDSLParser.FUNC_EQUILIBRIO, 0)

        def FUNC_MEDIANA(self):
            return self.getToken(HolocronDSLParser.FUNC_MEDIANA, 0)

        def FUNC_CENIT(self):
            return self.getToken(HolocronDSLParser.FUNC_CENIT, 0)

        def FUNC_NADIR(self):
            return self.getToken(HolocronDSLParser.FUNC_NADIR, 0)

        def FUNC_DESVIACION(self):
            return self.getToken(HolocronDSLParser.FUNC_DESVIACION, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_llamadaAgregacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaAgregacion" ):
                listener.enterLlamadaAgregacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaAgregacion" ):
                listener.exitLlamadaAgregacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaAgregacion" ):
                return visitor.visitLlamadaAgregacion(self)
            else:
                return visitor.visitChildren(self)




    def llamadaAgregacion(self):

        localctx = HolocronDSLParser.LlamadaAgregacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_llamadaAgregacion)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(HolocronDSLParser.FUNC_RECUENTO)
                self.state = 254
                self.match(HolocronDSLParser.LPAREN)
                self.state = 255
                self.match(HolocronDSLParser.RPAREN)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(HolocronDSLParser.FUNC_ACUMULAR)
                self.state = 257
                self.match(HolocronDSLParser.LPAREN)
                self.state = 258
                self.match(HolocronDSLParser.ID)
                self.state = 259
                self.match(HolocronDSLParser.RPAREN)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.match(HolocronDSLParser.FUNC_EQUILIBRIO)
                self.state = 261
                self.match(HolocronDSLParser.LPAREN)
                self.state = 262
                self.match(HolocronDSLParser.ID)
                self.state = 263
                self.match(HolocronDSLParser.RPAREN)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.match(HolocronDSLParser.FUNC_MEDIANA)
                self.state = 265
                self.match(HolocronDSLParser.LPAREN)
                self.state = 266
                self.match(HolocronDSLParser.ID)
                self.state = 267
                self.match(HolocronDSLParser.RPAREN)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 268
                self.match(HolocronDSLParser.FUNC_CENIT)
                self.state = 269
                self.match(HolocronDSLParser.LPAREN)
                self.state = 270
                self.match(HolocronDSLParser.ID)
                self.state = 271
                self.match(HolocronDSLParser.RPAREN)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 272
                self.match(HolocronDSLParser.FUNC_NADIR)
                self.state = 273
                self.match(HolocronDSLParser.LPAREN)
                self.state = 274
                self.match(HolocronDSLParser.ID)
                self.state = 275
                self.match(HolocronDSLParser.RPAREN)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 7)
                self.state = 276
                self.match(HolocronDSLParser.FUNC_DESVIACION)
                self.state = 277
                self.match(HolocronDSLParser.LPAREN)
                self.state = 278
                self.match(HolocronDSLParser.ID)
                self.state = 279
                self.match(HolocronDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionRegresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRAZAR_REGRESION(self):
            return self.getToken(HolocronDSLParser.TRAZAR_REGRESION, 0)

        def parametroRegresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.ParametroRegresionContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.ParametroRegresionContext,i)


        def LBRACK(self):
            return self.getToken(HolocronDSLParser.LBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.COMMA)
            else:
                return self.getToken(HolocronDSLParser.COMMA, i)

        def RBRACK(self):
            return self.getToken(HolocronDSLParser.RBRACK, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operacionRegresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionRegresion" ):
                listener.enterOperacionRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionRegresion" ):
                listener.exitOperacionRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionRegresion" ):
                return visitor.visitOperacionRegresion(self)
            else:
                return visitor.visitChildren(self)




    def operacionRegresion(self):

        localctx = HolocronDSLParser.OperacionRegresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operacionRegresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(HolocronDSLParser.TRAZAR_REGRESION)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 283
                self.match(HolocronDSLParser.LBRACK)


            self.state = 286
            self.parametroRegresion()
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 287
                    self.match(HolocronDSLParser.COMMA)
                    self.state = 288
                    self.parametroRegresion() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 294
                self.match(HolocronDSLParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaRegresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRAZAR_REGRESION(self):
            return self.getToken(HolocronDSLParser.TRAZAR_REGRESION, 0)

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def parametroRegresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.ParametroRegresionContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.ParametroRegresionContext,i)


        def LBRACK(self):
            return self.getToken(HolocronDSLParser.LBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.COMMA)
            else:
                return self.getToken(HolocronDSLParser.COMMA, i)

        def RBRACK(self):
            return self.getToken(HolocronDSLParser.RBRACK, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_sentenciaRegresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaRegresion" ):
                listener.enterSentenciaRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaRegresion" ):
                listener.exitSentenciaRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaRegresion" ):
                return visitor.visitSentenciaRegresion(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaRegresion(self):

        localctx = HolocronDSLParser.SentenciaRegresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_sentenciaRegresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(HolocronDSLParser.TRAZAR_REGRESION)
            self.state = 298
            self.match(HolocronDSLParser.ID)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 299
                self.match(HolocronDSLParser.LBRACK)


            self.state = 302
            self.parametroRegresion()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==73:
                self.state = 303
                self.match(HolocronDSLParser.COMMA)
                self.state = 304
                self.parametroRegresion()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 310
                self.match(HolocronDSLParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroRegresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EJE_X(self):
            return self.getToken(HolocronDSLParser.EJE_X, 0)

        def OP_ASIG(self):
            return self.getToken(HolocronDSLParser.OP_ASIG, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.ID)
            else:
                return self.getToken(HolocronDSLParser.ID, i)

        def EJE_Y(self):
            return self.getToken(HolocronDSLParser.EJE_Y, 0)

        def DESTINO(self):
            return self.getToken(HolocronDSLParser.DESTINO, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_parametroRegresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametroRegresion" ):
                listener.enterParametroRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametroRegresion" ):
                listener.exitParametroRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametroRegresion" ):
                return visitor.visitParametroRegresion(self)
            else:
                return visitor.visitChildren(self)




    def parametroRegresion(self):

        localctx = HolocronDSLParser.ParametroRegresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_parametroRegresion)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(HolocronDSLParser.EJE_X)
                self.state = 314
                self.match(HolocronDSLParser.OP_ASIG)
                self.state = 315
                self.match(HolocronDSLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(HolocronDSLParser.EJE_Y)
                self.state = 317
                self.match(HolocronDSLParser.OP_ASIG)
                self.state = 318
                self.match(HolocronDSLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.match(HolocronDSLParser.DESTINO)
                self.state = 320
                self.match(HolocronDSLParser.OP_ASIG)
                self.state = 321
                self.match(HolocronDSLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.match(HolocronDSLParser.ID)
                self.state = 323
                self.match(HolocronDSLParser.OP_ASIG)
                self.state = 324
                self.match(HolocronDSLParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 325
                self.match(HolocronDSLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaArchivadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCHIVAR_HOLOCRON(self):
            return self.getToken(HolocronDSLParser.ARCHIVAR_HOLOCRON, 0)

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def EN(self):
            return self.getToken(HolocronDSLParser.EN, 0)

        def CADENA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.CADENA)
            else:
                return self.getToken(HolocronDSLParser.CADENA, i)

        def DELIMITADO_POR(self):
            return self.getToken(HolocronDSLParser.DELIMITADO_POR, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_sentenciaArchivado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaArchivado" ):
                listener.enterSentenciaArchivado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaArchivado" ):
                listener.exitSentenciaArchivado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaArchivado" ):
                return visitor.visitSentenciaArchivado(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaArchivado(self):

        localctx = HolocronDSLParser.SentenciaArchivadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_sentenciaArchivado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(HolocronDSLParser.ARCHIVAR_HOLOCRON)
            self.state = 329
            self.match(HolocronDSLParser.ID)
            self.state = 330
            self.match(HolocronDSLParser.EN)
            self.state = 331
            self.match(HolocronDSLParser.CADENA)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 332
                self.match(HolocronDSLParser.DELIMITADO_POR)
                self.state = 333
                self.match(HolocronDSLParser.CADENA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaHologramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HOLOGRAMA(self):
            return self.getToken(HolocronDSLParser.HOLOGRAMA, 0)

        def tipoGrafica(self):
            return self.getTypedRuleContext(HolocronDSLParser.TipoGraficaContext,0)


        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def LBRACK(self):
            return self.getToken(HolocronDSLParser.LBRACK, 0)

        def propiedadHolograma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.PropiedadHologramaContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.PropiedadHologramaContext,i)


        def RBRACK(self):
            return self.getToken(HolocronDSLParser.RBRACK, 0)

        def FIN_HOLOGRAMA(self):
            return self.getToken(HolocronDSLParser.FIN_HOLOGRAMA, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_sentenciaHolograma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaHolograma" ):
                listener.enterSentenciaHolograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaHolograma" ):
                listener.exitSentenciaHolograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaHolograma" ):
                return visitor.visitSentenciaHolograma(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaHolograma(self):

        localctx = HolocronDSLParser.SentenciaHologramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_sentenciaHolograma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(HolocronDSLParser.HOLOGRAMA)
            self.state = 337
            self.tipoGrafica()
            self.state = 338
            self.match(HolocronDSLParser.ID)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 339
                self.match(HolocronDSLParser.LBRACK)


            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0):
                self.state = 342
                self.propiedadHolograma()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 348
                self.match(HolocronDSLParser.RBRACK)


            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 351
                self.match(HolocronDSLParser.FIN_HOLOGRAMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoGraficaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_BARRAS(self):
            return self.getToken(HolocronDSLParser.TIPO_BARRAS, 0)

        def TIPO_LINEAS(self):
            return self.getToken(HolocronDSLParser.TIPO_LINEAS, 0)

        def TIPO_DISPERSION(self):
            return self.getToken(HolocronDSLParser.TIPO_DISPERSION, 0)

        def TIPO_HISTOGRAMA(self):
            return self.getToken(HolocronDSLParser.TIPO_HISTOGRAMA, 0)

        def TIPO_CAJA(self):
            return self.getToken(HolocronDSLParser.TIPO_CAJA, 0)

        def TIPO_REGRESION(self):
            return self.getToken(HolocronDSLParser.TIPO_REGRESION, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_tipoGrafica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoGrafica" ):
                listener.enterTipoGrafica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoGrafica" ):
                listener.exitTipoGrafica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoGrafica" ):
                return visitor.visitTipoGrafica(self)
            else:
                return visitor.visitChildren(self)




    def tipoGrafica(self):

        localctx = HolocronDSLParser.TipoGraficaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_tipoGrafica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 541165879296) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropiedadHologramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EJE_X(self):
            return self.getToken(HolocronDSLParser.EJE_X, 0)

        def CADENA(self):
            return self.getToken(HolocronDSLParser.CADENA, 0)

        def OP_ASIG(self):
            return self.getToken(HolocronDSLParser.OP_ASIG, 0)

        def COMMA(self):
            return self.getToken(HolocronDSLParser.COMMA, 0)

        def EJE_Y(self):
            return self.getToken(HolocronDSLParser.EJE_Y, 0)

        def TITULO(self):
            return self.getToken(HolocronDSLParser.TITULO, 0)

        def GUARDAR(self):
            return self.getToken(HolocronDSLParser.GUARDAR, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_propiedadHolograma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropiedadHolograma" ):
                listener.enterPropiedadHolograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropiedadHolograma" ):
                listener.exitPropiedadHolograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropiedadHolograma" ):
                return visitor.visitPropiedadHolograma(self)
            else:
                return visitor.visitChildren(self)




    def propiedadHolograma(self):

        localctx = HolocronDSLParser.PropiedadHologramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_propiedadHolograma)
        self._la = 0 # Token type
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(HolocronDSLParser.EJE_X)
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 357
                    self.match(HolocronDSLParser.OP_ASIG)


                self.state = 360
                self.match(HolocronDSLParser.CADENA)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==73:
                    self.state = 361
                    self.match(HolocronDSLParser.COMMA)


                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(HolocronDSLParser.EJE_Y)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 365
                    self.match(HolocronDSLParser.OP_ASIG)


                self.state = 368
                self.match(HolocronDSLParser.CADENA)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==73:
                    self.state = 369
                    self.match(HolocronDSLParser.COMMA)


                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                self.match(HolocronDSLParser.TITULO)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 373
                    self.match(HolocronDSLParser.OP_ASIG)


                self.state = 376
                self.match(HolocronDSLParser.CADENA)
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==73:
                    self.state = 377
                    self.match(HolocronDSLParser.COMMA)


                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 380
                self.match(HolocronDSLParser.GUARDAR)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 381
                    self.match(HolocronDSLParser.OP_ASIG)


                self.state = 384
                self.match(HolocronDSLParser.CADENA)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==73:
                    self.state = 385
                    self.match(HolocronDSLParser.COMMA)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaCondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVALUAR_FUERZA(self):
            return self.getToken(HolocronDSLParser.EVALUAR_FUERZA, 0)

        def expresionBooleana(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionBooleanaContext,0)


        def SENDA_LUMINOSA(self):
            return self.getToken(HolocronDSLParser.SENDA_LUMINOSA, 0)

        def FIN_EVALUAR(self):
            return self.getToken(HolocronDSLParser.FIN_EVALUAR, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.SentenciaContext,i)


        def SENDA_OSCURA(self):
            return self.getToken(HolocronDSLParser.SENDA_OSCURA, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_sentenciaCondicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaCondicional" ):
                listener.enterSentenciaCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaCondicional" ):
                listener.exitSentenciaCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaCondicional" ):
                return visitor.visitSentenciaCondicional(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaCondicional(self):

        localctx = HolocronDSLParser.SentenciaCondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_sentenciaCondicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(HolocronDSLParser.EVALUAR_FUERZA)
            self.state = 391
            self.expresionBooleana(0)
            self.state = 392
            self.match(HolocronDSLParser.SENDA_LUMINOSA)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 431010709766210) != 0) or _la==77:
                self.state = 393
                self.sentencia()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 399
                self.match(HolocronDSLParser.SENDA_OSCURA)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 431010709766210) != 0) or _la==77:
                    self.state = 400
                    self.sentencia()
                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 408
            self.match(HolocronDSLParser.FIN_EVALUAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaTransmisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionPipeline(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionPipelineContext,0)


        def TRANSMITIR(self):
            return self.getToken(HolocronDSLParser.TRANSMITIR, 0)

        def MOSTRAR(self):
            return self.getToken(HolocronDSLParser.MOSTRAR, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_sentenciaTransmision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaTransmision" ):
                listener.enterSentenciaTransmision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaTransmision" ):
                listener.exitSentenciaTransmision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaTransmision" ):
                return visitor.visitSentenciaTransmision(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaTransmision(self):

        localctx = HolocronDSLParser.SentenciaTransmisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_sentenciaTransmision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            _la = self._input.LA(1)
            if not(_la==47 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 411
            self.expresionPipeline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionBooleanaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_expresionBooleana

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprBoolOrContext(ExpresionBooleanaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.ExpresionBooleanaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresionBooleana(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionBooleanaContext,0)

        def terminoBooleano(self):
            return self.getTypedRuleContext(HolocronDSLParser.TerminoBooleanoContext,0)

        def O_LOGICO(self):
            return self.getToken(HolocronDSLParser.O_LOGICO, 0)
        def O_FUERZA(self):
            return self.getToken(HolocronDSLParser.O_FUERZA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolOr" ):
                listener.enterExprBoolOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolOr" ):
                listener.exitExprBoolOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolOr" ):
                return visitor.visitExprBoolOr(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolTerminoContext(ExpresionBooleanaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.ExpresionBooleanaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terminoBooleano(self):
            return self.getTypedRuleContext(HolocronDSLParser.TerminoBooleanoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolTermino" ):
                listener.enterExprBoolTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolTermino" ):
                listener.exitExprBoolTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolTermino" ):
                return visitor.visitExprBoolTermino(self)
            else:
                return visitor.visitChildren(self)



    def expresionBooleana(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HolocronDSLParser.ExpresionBooleanaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expresionBooleana, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HolocronDSLParser.ExprBoolTerminoContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 414
            self.terminoBooleano(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HolocronDSLParser.ExprBoolOrContext(self, HolocronDSLParser.ExpresionBooleanaContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresionBooleana)
                    self.state = 416
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 417
                    _la = self._input.LA(1)
                    if not(_la==51 or _la==52):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 418
                    self.terminoBooleano(0) 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoBooleanoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_terminoBooleano

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprBoolAndContext(TerminoBooleanoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.TerminoBooleanoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terminoBooleano(self):
            return self.getTypedRuleContext(HolocronDSLParser.TerminoBooleanoContext,0)

        def factorBooleano(self):
            return self.getTypedRuleContext(HolocronDSLParser.FactorBooleanoContext,0)

        def Y_LOGICO(self):
            return self.getToken(HolocronDSLParser.Y_LOGICO, 0)
        def Y_FUERZA(self):
            return self.getToken(HolocronDSLParser.Y_FUERZA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolAnd" ):
                listener.enterExprBoolAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolAnd" ):
                listener.exitExprBoolAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolAnd" ):
                return visitor.visitExprBoolAnd(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolFactorContext(TerminoBooleanoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.TerminoBooleanoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factorBooleano(self):
            return self.getTypedRuleContext(HolocronDSLParser.FactorBooleanoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolFactor" ):
                listener.enterExprBoolFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolFactor" ):
                listener.exitExprBoolFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolFactor" ):
                return visitor.visitExprBoolFactor(self)
            else:
                return visitor.visitChildren(self)



    def terminoBooleano(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HolocronDSLParser.TerminoBooleanoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_terminoBooleano, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HolocronDSLParser.ExprBoolFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 425
            self.factorBooleano()
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HolocronDSLParser.ExprBoolAndContext(self, HolocronDSLParser.TerminoBooleanoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terminoBooleano)
                    self.state = 427
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 428
                    _la = self._input.LA(1)
                    if not(_la==49 or _la==50):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 429
                    self.factorBooleano() 
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorBooleanoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_factorBooleano

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprBoolComparacionContext(FactorBooleanoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.FactorBooleanoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparacionRelacional(self):
            return self.getTypedRuleContext(HolocronDSLParser.ComparacionRelacionalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolComparacion" ):
                listener.enterExprBoolComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolComparacion" ):
                listener.exitExprBoolComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolComparacion" ):
                return visitor.visitExprBoolComparacion(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolLiteralContext(FactorBooleanoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.FactorBooleanoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(HolocronDSLParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolLiteral" ):
                listener.enterExprBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolLiteral" ):
                listener.exitExprBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolLiteral" ):
                return visitor.visitExprBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolParentesisContext(FactorBooleanoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.FactorBooleanoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(HolocronDSLParser.LPAREN, 0)
        def expresionBooleana(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionBooleanaContext,0)

        def RPAREN(self):
            return self.getToken(HolocronDSLParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolParentesis" ):
                listener.enterExprBoolParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolParentesis" ):
                listener.exitExprBoolParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolParentesis" ):
                return visitor.visitExprBoolParentesis(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolNotContext(FactorBooleanoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.FactorBooleanoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factorBooleano(self):
            return self.getTypedRuleContext(HolocronDSLParser.FactorBooleanoContext,0)

        def NO_LOGICO(self):
            return self.getToken(HolocronDSLParser.NO_LOGICO, 0)
        def NO_FUERZA(self):
            return self.getToken(HolocronDSLParser.NO_FUERZA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolNot" ):
                listener.enterExprBoolNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolNot" ):
                listener.exitExprBoolNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolNot" ):
                return visitor.visitExprBoolNot(self)
            else:
                return visitor.visitChildren(self)



    def factorBooleano(self):

        localctx = HolocronDSLParser.FactorBooleanoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_factorBooleano)
        self._la = 0 # Token type
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = HolocronDSLParser.ExprBoolNotContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                _la = self._input.LA(1)
                if not(_la==53 or _la==54):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 436
                self.factorBooleano()
                pass

            elif la_ == 2:
                localctx = HolocronDSLParser.ExprBoolComparacionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.comparacionRelacional()
                pass

            elif la_ == 3:
                localctx = HolocronDSLParser.ExprBoolParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(HolocronDSLParser.LPAREN)
                self.state = 439
                self.expresionBooleana(0)
                self.state = 440
                self.match(HolocronDSLParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = HolocronDSLParser.ExprBoolLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 442
                self.match(HolocronDSLParser.BOOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HolocronDSLParser.ExpresionAritmeticaContext)
            else:
                return self.getTypedRuleContext(HolocronDSLParser.ExpresionAritmeticaContext,i)


        def operadorRelacional(self):
            return self.getTypedRuleContext(HolocronDSLParser.OperadorRelacionalContext,0)


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_comparacionRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacionRelacional" ):
                listener.enterComparacionRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacionRelacional" ):
                listener.exitComparacionRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacionRelacional" ):
                return visitor.visitComparacionRelacional(self)
            else:
                return visitor.visitChildren(self)




    def comparacionRelacional(self):

        localctx = HolocronDSLParser.ComparacionRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_comparacionRelacional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.expresionAritmetica(0)
            self.state = 446
            self.operadorRelacional()
            self.state = 447
            self.expresionAritmetica(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_IGUAL(self):
            return self.getToken(HolocronDSLParser.OP_IGUAL, 0)

        def OP_DIFERENTE(self):
            return self.getToken(HolocronDSLParser.OP_DIFERENTE, 0)

        def OP_MENOR_IGUAL(self):
            return self.getToken(HolocronDSLParser.OP_MENOR_IGUAL, 0)

        def OP_MAYOR_IGUAL(self):
            return self.getToken(HolocronDSLParser.OP_MAYOR_IGUAL, 0)

        def OP_MENOR(self):
            return self.getToken(HolocronDSLParser.OP_MENOR, 0)

        def OP_MAYOR(self):
            return self.getToken(HolocronDSLParser.OP_MAYOR, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_operadorRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorRelacional" ):
                listener.enterOperadorRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorRelacional" ):
                listener.exitOperadorRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorRelacional" ):
                return visitor.visitOperadorRelacional(self)
            else:
                return visitor.visitChildren(self)




    def operadorRelacional(self):

        localctx = HolocronDSLParser.OperadorRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operadorRelacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9079256848778919936) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionAritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_expresionAritmetica

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprAritTerminoContext(ExpresionAritmeticaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.ExpresionAritmeticaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terminoAritmetico(self):
            return self.getTypedRuleContext(HolocronDSLParser.TerminoAritmeticoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritTermino" ):
                listener.enterExprAritTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritTermino" ):
                listener.exitExprAritTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritTermino" ):
                return visitor.visitExprAritTermino(self)
            else:
                return visitor.visitChildren(self)


    class ExprAritSumaRestaContext(ExpresionAritmeticaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.ExpresionAritmeticaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresionAritmetica(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionAritmeticaContext,0)

        def terminoAritmetico(self):
            return self.getTypedRuleContext(HolocronDSLParser.TerminoAritmeticoContext,0)

        def OP_SUMA(self):
            return self.getToken(HolocronDSLParser.OP_SUMA, 0)
        def OP_RESTA(self):
            return self.getToken(HolocronDSLParser.OP_RESTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritSumaResta" ):
                listener.enterExprAritSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritSumaResta" ):
                listener.exitExprAritSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritSumaResta" ):
                return visitor.visitExprAritSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def expresionAritmetica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HolocronDSLParser.ExpresionAritmeticaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expresionAritmetica, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HolocronDSLParser.ExprAritTerminoContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 452
            self.terminoAritmetico(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HolocronDSLParser.ExprAritSumaRestaContext(self, HolocronDSLParser.ExpresionAritmeticaContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresionAritmetica)
                    self.state = 454
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 455
                    _la = self._input.LA(1)
                    if not(_la==63 or _la==64):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 456
                    self.terminoAritmetico(0) 
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoAritmeticoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_terminoAritmetico

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprAritMultDivContext(TerminoAritmeticoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.TerminoAritmeticoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terminoAritmetico(self):
            return self.getTypedRuleContext(HolocronDSLParser.TerminoAritmeticoContext,0)

        def factorPotencia(self):
            return self.getTypedRuleContext(HolocronDSLParser.FactorPotenciaContext,0)

        def OP_MULT(self):
            return self.getToken(HolocronDSLParser.OP_MULT, 0)
        def OP_DIV(self):
            return self.getToken(HolocronDSLParser.OP_DIV, 0)
        def OP_MOD(self):
            return self.getToken(HolocronDSLParser.OP_MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritMultDiv" ):
                listener.enterExprAritMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritMultDiv" ):
                listener.exitExprAritMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritMultDiv" ):
                return visitor.visitExprAritMultDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprAritFactorContext(TerminoAritmeticoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.TerminoAritmeticoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factorPotencia(self):
            return self.getTypedRuleContext(HolocronDSLParser.FactorPotenciaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritFactor" ):
                listener.enterExprAritFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritFactor" ):
                listener.exitExprAritFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritFactor" ):
                return visitor.visitExprAritFactor(self)
            else:
                return visitor.visitChildren(self)



    def terminoAritmetico(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HolocronDSLParser.TerminoAritmeticoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_terminoAritmetico, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HolocronDSLParser.ExprAritFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 463
            self.factorPotencia()
            self._ctx.stop = self._input.LT(-1)
            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HolocronDSLParser.ExprAritMultDivContext(self, HolocronDSLParser.TerminoAritmeticoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terminoAritmetico)
                    self.state = 465
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 466
                    _la = self._input.LA(1)
                    if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 7) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 467
                    self.factorPotencia() 
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorPotenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_factorPotencia

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprAritPotenciaContext(FactorPotenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.FactorPotenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomoAritmetico(self):
            return self.getTypedRuleContext(HolocronDSLParser.AtomoAritmeticoContext,0)

        def OP_POTENCIA(self):
            return self.getToken(HolocronDSLParser.OP_POTENCIA, 0)
        def factorPotencia(self):
            return self.getTypedRuleContext(HolocronDSLParser.FactorPotenciaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritPotencia" ):
                listener.enterExprAritPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritPotencia" ):
                listener.exitExprAritPotencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritPotencia" ):
                return visitor.visitExprAritPotencia(self)
            else:
                return visitor.visitChildren(self)



    def factorPotencia(self):

        localctx = HolocronDSLParser.FactorPotenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_factorPotencia)
        try:
            localctx = HolocronDSLParser.ExprAritPotenciaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.atomoAritmetico()
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 474
                self.match(HolocronDSLParser.OP_POTENCIA)
                self.state = 475
                self.factorPotencia()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomoAritmeticoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HolocronDSLParser.RULE_atomoAritmetico

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomoCadenaContext(AtomoAritmeticoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.AtomoAritmeticoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CADENA(self):
            return self.getToken(HolocronDSLParser.CADENA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomoCadena" ):
                listener.enterAtomoCadena(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomoCadena" ):
                listener.exitAtomoCadena(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomoCadena" ):
                return visitor.visitAtomoCadena(self)
            else:
                return visitor.visitChildren(self)


    class AtomoIdentificadorContext(AtomoAritmeticoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.AtomoAritmeticoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HolocronDSLParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomoIdentificador" ):
                listener.enterAtomoIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomoIdentificador" ):
                listener.exitAtomoIdentificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomoIdentificador" ):
                return visitor.visitAtomoIdentificador(self)
            else:
                return visitor.visitChildren(self)


    class AtomoParentesisContext(AtomoAritmeticoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.AtomoAritmeticoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(HolocronDSLParser.LPAREN, 0)
        def expresionAritmetica(self):
            return self.getTypedRuleContext(HolocronDSLParser.ExpresionAritmeticaContext,0)

        def RPAREN(self):
            return self.getToken(HolocronDSLParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomoParentesis" ):
                listener.enterAtomoParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomoParentesis" ):
                listener.exitAtomoParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomoParentesis" ):
                return visitor.visitAtomoParentesis(self)
            else:
                return visitor.visitChildren(self)


    class AtomoNumeroContext(AtomoAritmeticoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.AtomoAritmeticoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(HolocronDSLParser.NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomoNumero" ):
                listener.enterAtomoNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomoNumero" ):
                listener.exitAtomoNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomoNumero" ):
                return visitor.visitAtomoNumero(self)
            else:
                return visitor.visitChildren(self)


    class AtomoBooleanoContext(AtomoAritmeticoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HolocronDSLParser.AtomoAritmeticoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(HolocronDSLParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomoBooleano" ):
                listener.enterAtomoBooleano(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomoBooleano" ):
                listener.exitAtomoBooleano(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomoBooleano" ):
                return visitor.visitAtomoBooleano(self)
            else:
                return visitor.visitChildren(self)



    def atomoAritmetico(self):

        localctx = HolocronDSLParser.AtomoAritmeticoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_atomoAritmetico)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [75]:
                localctx = HolocronDSLParser.AtomoNumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(HolocronDSLParser.NUMERO)
                pass
            elif token in [76]:
                localctx = HolocronDSLParser.AtomoCadenaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(HolocronDSLParser.CADENA)
                pass
            elif token in [74]:
                localctx = HolocronDSLParser.AtomoBooleanoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                self.match(HolocronDSLParser.BOOL)
                pass
            elif token in [77]:
                localctx = HolocronDSLParser.AtomoIdentificadorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 481
                self.match(HolocronDSLParser.ID)
                pass
            elif token in [69]:
                localctx = HolocronDSLParser.AtomoParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 482
                self.match(HolocronDSLParser.LPAREN)
                self.state = 483
                self.expresionAritmetica(0)
                self.state = 484
                self.match(HolocronDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdentificadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.ID)
            else:
                return self.getToken(HolocronDSLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HolocronDSLParser.COMMA)
            else:
                return self.getToken(HolocronDSLParser.COMMA, i)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_listaIdentificadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIdentificadores" ):
                listener.enterListaIdentificadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIdentificadores" ):
                listener.exitListaIdentificadores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaIdentificadores" ):
                return visitor.visitListaIdentificadores(self)
            else:
                return visitor.visitChildren(self)




    def listaIdentificadores(self):

        localctx = HolocronDSLParser.ListaIdentificadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_listaIdentificadores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(HolocronDSLParser.ID)
            self.state = 493
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 489
                    self.match(HolocronDSLParser.COMMA)
                    self.state = 490
                    self.match(HolocronDSLParser.ID) 
                self.state = 495
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(HolocronDSLParser.NUMERO, 0)

        def CADENA(self):
            return self.getToken(HolocronDSLParser.CADENA, 0)

        def BOOL(self):
            return self.getToken(HolocronDSLParser.BOOL, 0)

        def getRuleIndex(self):
            return HolocronDSLParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = HolocronDSLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            _la = self._input.LA(1)
            if not(((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.expresionBooleana_sempred
        self._predicates[34] = self.terminoBooleano_sempred
        self._predicates[38] = self.expresionAritmetica_sempred
        self._predicates[39] = self.terminoAritmetico_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresionBooleana_sempred(self, localctx:ExpresionBooleanaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def terminoBooleano_sempred(self, localctx:TerminoBooleanoContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expresionAritmetica_sempred(self, localctx:ExpresionAritmeticaContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def terminoAritmetico_sempred(self, localctx:TerminoAritmeticoContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




