transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/ula_fx.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/stack_pointer.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/proc_fx.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/prefetch.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/pc.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/positivo_fx.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/mem_instr.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/mem_data.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/instr_dec_fx.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/core_fx.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Proc_IP/addr_dec.v}
vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/procfixcba_H {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/procfixcba_H/procfixcba.v}

vlog -vlog01compat -work work +incdir+C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Quartus_Files {C:/Users/LuccaViccini/Desktop/UFJF/IC/VIC_CERN/CBA/procfixcba/Hardware/Quartus_Files/procfixcba_tb.v}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L cycloneiv_hssi_ver -L cycloneiv_pcie_hip_ver -L cycloneiv_ver -L rtl_work -L work -voptargs="+acc"  procfixcba_tb

add wave *
view structure
view signals
run 1 ps
