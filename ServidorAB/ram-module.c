#include <linux/module.h>
#include <linux/init.h>
#include <linux/proc_fs.h>
#include <linux/sched.h>
#include <linux/uaccess.h>
#include <linux/fs.h>
#include <linux/sysinfo.h>
#include <linux/seq_file.h>
#include <linux/slab.h>
#include <linux/mm.h>
#include <linux/swap.h>
#include <linux/rbtree.h>
#include <linux/hugetlb.h>
#include <linux/mman.h>
#include <linux/mmzone.h>
#include <linux/swap.h>
#include <linux/vmstat.h>
#include <linux/atomic.h>
#include <asm/page.h>
#include <asm/pgtable.h>

struct sysinfo i;
int lru;


static int my_proc_show(struct seq_file *m, void *v){
    #define K(x) ((x) << (PAGE_SHIFT - 10))
    si_meminfo(&i);
    seq_printf(m,"%8lu-%8lu",K(i.totalram),K(i.freeram));    
    return 0;   
}

static ssize_t my_proc_write(struct file* file, const char __user *buffer, size_t count, loff_t *f_pos){
    return 0;
}

static int my_proc_open(struct inode *inode, struct file *file){
    return single_open(file, my_proc_show ,NULL);
}

static struct file_operations my_fops = {
    .owner = THIS_MODULE,
    .open = my_proc_open,
    .release = single_release,
    .read = seq_read,
    .llseek = seq_lseek,
    .write = my_proc_write
};

static int __init test_init(void){
    struct proc_dir_entry *entry;
    entry = proc_create("ram-module", 0777, NULL, &my_fops);
    if(!entry){
        return -1;
    } else {
        printk(KERN_INFO "Inicio\n");
    }
    return 0;
}

static void __exit test_exit(void){
    remove_proc_entry("ram-module", NULL);
    printk(KERN_INFO "Final\n");
}

module_init(test_init);
module_exit(test_exit);
MODULE_LICENSE("GPL");