import { client, publicSDK } from "@devrev/typescript-sdk";

export async function handleEvent(
  event: any,
) {
  const devrevPAT = event.context.secrets.service_account_token;
  const APIBase = event.execution_metadata.devrev_endpoint;
  const devrevSDK = client.setup({
    endpoint: APIBase,
    token: devrevPAT,
  })
  try {

    // CHANGES MADE
    const workCreated = event.payload.work_created.work;
    let bodyComment = 'Hello World!!! Event ' + workCreated.display_id + ' has been created ';

    const body = {
      object: workCreated.id,
      type: 'timeline_comment',
      body: bodyComment,
    }
    
    const response = await devrevSDK.timelineEntriesCreate(body as any);
    return response;

  } catch (error) {
    console.log(error);
    return error;
  }
}

export const run = async (events: any[]) => {
  
  //ADDITION OF CONSOLE STATEMENT
  console.info(`Hello World!!! Event ${events[0].payload.work_created.work.display_id} has been created`);
  for (let event of events) {
    await handleEvent(event);
  }
};

export default run;
