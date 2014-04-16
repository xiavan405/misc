#include <iostream>

#include <bam/sam.h>
#include <bam/bam.h>

using namespace std;

int main() {
	samfile_t* h = samopen("/home/xiavan/test/SRR427097.bam", "r", NULL);

	bam1_t* b = new bam1_t;
	bam1_core_t c;
	while (samread(h, b)) {
		c = b->core;
		cout  << c.tid << " " << c.pos << endl;
	}
	delete b;
	cout << "done" << endl;
	samclose(h);
}
