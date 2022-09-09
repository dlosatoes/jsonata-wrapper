#include <string>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "jsonata-es5.h"
#include "duktape.h"

static void my_duk_abort(void * udata, const char *msg) {
    abort();
}

class DukContext {
    duk_context *ctx;
  public:
    DukContext():ctx(duk_create_heap(NULL, NULL, NULL, NULL, my_duk_abort)) {
        if (duk_peval_string(ctx, JAVASCRIP_JSONATA_LIB.c_str()) != 0) {
            abort();
        }	
    };
    ~DukContext() {
        duk_destroy_heap(ctx);
    };
    std::string jsonata_call(std::string xform, std::string json_data) {
	std::string command = std::string("JSON.stringify(jsonata('") + xform + std::string("').evaluate(") + json_data + std::string("));");
        if (duk_peval_string(ctx, command.c_str()) != 0) {
           abort();
	}
	return duk_safe_to_string(ctx, -1);
    }
};

std::string jsonata_wrapper_cpp(std::string xform, std::string json_data) {
    DukContext myctx;
    return myctx.jsonata_call(xform, json_data);
}

PYBIND11_MODULE(jsonata, m) {
    m.doc() = "Python Wrapper for JDONata JavaScript library";
    m.def("transform", &jsonata_wrapper_cpp, "Apply JSONata transform to JSON data and returnt the result.",
          pybind11::arg("xform"), pybind11::arg("json_data"));
}



