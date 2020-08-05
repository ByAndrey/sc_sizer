from flask import Flask, request, render_template

app = Flask(__name__)

def size(Rprs,Vm,CR,Rs,Rh,Rd):
    result = Rprs*(Vm*((24*CR*Rs)+(24*Rh)+Rd))
    return(result)

@app.route("/", methods=['GET','POST'])
def main_page():
    #default
    Rprs=200
    Vm=100
    CR=12
    Rs=14
    Rh=28
    Rd=84
    if (request.args.get('Rprs')):
        #num_stor=request.args.get('num_stor')
        Rprs=request.args.get('Rprs')
        Vm=request.args.get('Vm')
        CR=request.args.get('CR')
        Rs=request.args.get('Rs')
        Rh=request.args.get('Rh')
        Rd=request.args.get('Rd')
        result=size(int(Rprs),int(Vm),int(CR),int(Rs),int(Rh),int(Rd))
        print(result)
    else:
        if (not Rprs):
            Rprs=200
        if (not Vm):
            Vm=100
        if (not CR):
            CR=12
        if (not Rs):
            Rs=14
        if (not Rh):
            Rh=28
        if (not Rd):
            Rd=84
        result=size(int(Rprs),int(Vm),int(CR),int(Rs),int(Rh),int(Rd))
    return render_template("sizer.html", Rprs=Rprs, Vm=Vm, CR=CR, Rs=Rs, Rh=Rh, Rd=Rd, result=result)

if __name__ == "__main__":
   app.run(debug="True", port=80)